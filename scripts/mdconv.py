# -*- coding: utf-8 -*-
"""
HTML(s) -> Markdown 转换核心。
针对 Nextra 2 / nextra-theme-docs 生成的结构：
  article > main  (第一子元素是面包屑，末尾是上一页/下一页导航)
  h1..h6 / p / pre[data-language]>code>span.line / table(thead,tbody) /
  div.nextra-callout(按边框颜色区分 note|warning|error) / ul / ol / hr / img
内部链接先转成占位符 @@LINK:route#frag@@，第二阶段再按目标文件解析成相对路径，
这样同一份 Markdown 既能整页输出，也能拆分成单条 API 文件。
"""
import io, json, os, re
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

SKIP_EXACT_CLASSES = {"nextra-breadcrumb", "nx-mt-16"}
LANG_MAP = {"py": "python", "python": "python", "sh": "bash", "shell": "bash",
            "js": "javascript", "ts": "typescript", "json": "json", "toml": "toml",
            "ini": "ini", "yaml": "yaml", "bat": "bat", "powershell": "powershell"}

CALLOUT_MAP = [
    ("red", "CAUTION"), ("yellow", "WARNING"), ("green", "TIP"),
    ("blue", "NOTE"), ("gray", "NOTE"), ("orange", "WARNING"),
]


def norm(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


class Converter:
    def __init__(self, route, title, anchors=None):
        self.route = route
        self.title = title
        self.anchors = anchors or {}   # id(标题元素) -> 官方锚点名

    # ---------- 块级 ----------
    def blocks(self, node):
        out = []
        for child in node.children:
            if isinstance(child, NavigableString):
                txt = norm(str(child))
                if txt:
                    out.append(txt)
                continue
            if not isinstance(child, Tag):
                continue
            out.extend(self.block(child))
        return out

    def _skippable(self, el):
        cls = set(el.get("class") or [])
        if cls & SKIP_EXACT_CLASSES:
            return True
        # 上一页 / 下一页 导航条
        if "nx-border-t" in cls and "nx-mb-8" in cls and "nx-flex" in cls:
            return True
        # 纯占位 span
        if el.name == "span" and cls <= {"w-px", "h-px", "block"}:
            return True
        return False

    def block(self, el):
        if self._skippable(el):
            return []
        name = el.name
        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            lvl = int(name[1])
            head = "#" * lvl + " " + self.inline(el)
            anchor = self.anchors.get(id(el))
            if anchor:
                return [f'<a id="{anchor}"></a>\n{head}']
            return [head]
        if name == "p":
            t = self.inline(el).strip()
            return [t] if t else []
        if name == "pre":
            return [self.code_block(el)]
        if name == "table":
            return [self.table(el)]
        if name in ("ul", "ol"):
            return [self.list_block(el, 0)]
        if name == "hr":
            return ["---"]
        if name == "blockquote":
            inner = "\n".join(self.blocks(el)).strip()
            return ["\n".join("> " + l for l in inner.splitlines())] if inner else []
        if name == "img":
            return [self.img(el)]
        if name == "br":
            return []
        if name == "div":
            cls = set(el.get("class") or [])
            if "nextra-callout" in cls:
                return self.callout(el)
            if "nextra-filetree" in cls:
                return [self.filetree(el)]
            if "nextra-code-block" in cls:
                fn = None
                for c in el.find_all("div", recursive=False):
                    if "nx-absolute" in set(c.get("class") or []):
                        fn = norm(c.get_text())
                        break
                pre = el.find("pre")
                if pre is None:
                    return self.blocks(el)
                out = []
                if fn:
                    out.append(f"**`{fn}`**")
                out.append(self.code_block(pre))
                return out
            # HeroUI 表格壳、mermaid 壳等：继续下钻
            return self.blocks(el)
        if name == "span":
            if "nx-sr-only" in set(el.get("class") or []):
                return []
            t = self.inline(el).strip()
            return [t] if t else []
        # 其它容器一律下钻
        return self.blocks(el)

    def callout(self, el):
        cls = set(el.get("class") or [])
        kind = "NOTE"
        for key, val in CALLOUT_MAP:
            if any(key in c for c in cls):
                kind = val
                break
        body = []
        for child in el.children:
            if not isinstance(child, Tag):
                continue
            if "nx-select-none" in set(child.get("class") or []):
                continue  # 图标
            body.extend(self.blocks(child))
        # 首段若与标题重复则去掉
        text = "\n\n".join(b for b in body if b.strip())
        if not text.strip():
            return []
        lines = []
        first = True
        for para in text.split("\n\n"):
            para = para.strip()
            if not para:
                continue
            if first:
                lines.append(f"> [!{kind}]")
                first = False
            for l in para.splitlines():
                lines.append("> " + l if l.strip() else ">")
            lines.append(">")
        while lines and lines[-1] == ">":
            lines.pop()
        return ["\n".join(lines)]

    def filetree(self, el):
        """Nextra 的可折叠目录树 -> 缩进代码块（保留层级，纯文本好检索）"""
        lines = []

        def label(li):
            b = li.find("button", recursive=False) or li.find("span", recursive=False)
            return norm(b.get_text()) if b is not None else ""

        def walk(ul, prefix):
            items = ul.find_all("li", recursive=False)
            for i, li in enumerate(items):
                last = i == len(items) - 1
                lines.append(prefix + ("└── " if last else "├── ") + label(li))
                sub = li.find("ul", recursive=False)
                if sub is not None:
                    walk(sub, prefix + ("    " if last else "│   "))

        # 根层 = 不在任何 <ul> 里的 <li>
        roots = [li for li in el.find_all("li") if li.find_parent("ul") is None]
        for li in roots:
            lines.append(label(li))
            sub = li.find("ul", recursive=False)
            if sub is not None:
                walk(sub, "")
        if not lines:
            return ""
        return f"```text\n{chr(10).join(lines)}\n```"

    def code_block(self, pre):
        code = pre.find("code")
        target = code if code is not None else pre
        lang = (pre.get("data-language") or target.get("data-language") or "text").lower()
        lang = LANG_MAP.get(lang, lang)
        text = target.get_text()
        text = text.replace("\r\n", "\n").replace("\xa0", " ")
        text = "\n".join(l.rstrip() for l in text.split("\n")).strip("\n")
        fence = "```"
        while fence in text:
            fence += "`"
        return f"{fence}{lang}\n{text}\n{fence}"

    def table(self, tbl):
        head, rows = [], []
        thead = tbl.find("thead")
        if thead is not None:
            for tr in thead.find_all("tr"):
                cells = [self.cell(c) for c in tr.find_all(["th", "td"], recursive=False)]
                if cells and not head:
                    head = cells
        tbody = tbl.find("tbody")
        body_rows = tbody.find_all("tr", recursive=False) if tbody is not None else []
        if not body_rows:
            body_rows = [tr for tr in tbl.find_all("tr") if tr.find("td")]
        for tr in body_rows:
            cells = [self.cell(c) for c in tr.find_all(["th", "td"], recursive=False)]
            if cells and any(cells):
                rows.append(cells)
        if not head:
            if not rows:
                return ""
            head, rows = rows[0], rows[1:]
        ncol = max([len(head)] + [len(r) for r in rows]) if (head or rows) else 0
        if ncol == 0:
            return ""
        head += [""] * (ncol - len(head))
        out = ["| " + " | ".join(head) + " |", "|" + "|".join([" --- "] * ncol) + "|"]
        for r in rows:
            r = r + [""] * (ncol - len(r))
            out.append("| " + " | ".join(r) + " |")
        return "\n".join(out)

    def cell(self, td):
        t = self.inline(td)
        t = t.replace("\n", "<br>").replace("|", "\\|")
        t = re.sub(r"\s{2,}", " ", t).strip()
        return t

    def list_block(self, el, depth):
        ordered = el.name == "ol"
        items = []
        for i, li in enumerate(el.find_all("li", recursive=False), 1):
            marker = f"{i}." if ordered else "-"
            sub = []
            inline_parts = []
            for child in li.children:
                if isinstance(child, NavigableString):
                    inline_parts.append(str(child))
                elif isinstance(child, Tag) and child.name in ("ul", "ol"):
                    sub.append(self.list_block(child, depth + 1))
                elif isinstance(child, Tag) and child.name == "p":
                    inline_parts.append(self.inline(child).strip())
                elif isinstance(child, Tag) and child.name == "pre":
                    sub.append(self.code_block(child))
                else:
                    inline_parts.append(self.inline(child))
            text = " ".join(x for x in inline_parts if x).strip()
            text = re.sub(r"[ \t]{2,}", " ", text)
            line = "  " * depth + f"{marker} {text}"
            items.append(line)
            for s in sub:
                s = s.strip("\n")
                if s:
                    items.append("\n".join("  " * (depth + 1) + l if l.strip() else l
                                           for l in s.splitlines()))
        return "\n".join(items)

    def img(self, el):
        src = el.get("src") or ""
        alt = el.get("alt") or ""
        return f"![{alt}]({src})"

    # ---------- 行内 ----------
    def inline(self, node):
        parts = []
        for child in node.children:
            if isinstance(child, NavigableString):
                parts.append(str(child))
                continue
            if not isinstance(child, Tag):
                continue
            name = child.name
            if name in ("svg", "script", "style"):
                continue
            if name == "span" and "nx-sr-only" in set(child.get("class") or []):
                continue
            if name == "a" and "subheading-anchor" in set(child.get("class") or []):
                continue
            if name == "code":
                parts.append(self.inline_code(child.get_text()))
            elif name in ("strong", "b"):
                inner = self.inline(child)
                parts.append(f"**{inner}**" if inner.strip() else inner)
            elif name in ("em", "i"):
                inner = self.inline(child)
                parts.append(f"*{inner}*" if inner.strip() else inner)
            elif name in ("del", "s"):
                parts.append(f"~~{self.inline(child)}~~")
            elif name == "a":
                parts.append(self.link(child))
            elif name == "br":
                parts.append("\n")
            elif name == "img":
                parts.append(self.img(child))
            elif name == "kbd":
                parts.append("`" + child.get_text().strip() + "`")
            elif name in ("sup", "sub"):
                parts.append(f"<{name}>{self.inline(child)}</{name}>")
            else:
                parts.append(self.inline(child))
        text = "".join(parts)
        # 折叠空白（保留单个换行 → 空格，双换行由块级控制）
        text = re.sub(r"[ \t\u00a0]+", " ", text)
        text = re.sub(r" *\n *", "\n", text)
        return text

    def inline_code(self, txt):
        txt = txt.replace("\n", " ")
        fence = "`"
        while fence in txt:
            fence += "`"
        pad = " " if txt.startswith("`") or txt.endswith("`") else ""
        return f"{fence}{pad}{txt}{pad}{fence}"

    def link(self, a):
        href = (a.get("href") or "").strip()
        text = self.inline(a).strip()
        if not href:
            return text
        if href.startswith("#"):
            # Nextra 标题自带的自链接锚点（# 图标），正文里由 <a id> 代替
            if not re.sub(r"[#\s\u200b]", "", text):
                return ""
            return f"[{text}](@@LINK:#{href[1:]}@@)"
        m = re.match(r"^/pythongo_v2/?(.*)$", href)
        if m:
            target = m.group(1)
            route, _, frag = target.partition("#")
            route = "/" + route.strip("/") if route.strip("/") else "/"
            return f"[{text}](@@LINK:{route}#{frag}@@)"
        return f"[{text}]({href})"


def parse_page(html_path, route, title):
    soup = BeautifulSoup(io.open(html_path, encoding="utf-8").read(), "lxml")
    main = soup.select_one("article main")
    if main is None:
        main = soup.select_one("main")
    conv = Converter(route, title)
    blocks = conv.blocks(main)
    # 去掉空块
    blocks = [b for b in blocks if b is not None and str(b).strip()]
    return blocks
