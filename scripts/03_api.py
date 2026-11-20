# -*- coding: utf-8 -*-
"""06：把 docs/ 里的 API 页拆成「一条 API 一个文件」的速查卡（api/），
并给每个模块生成 _index.md。拆分的同时把相对链接重新定位到新位置。"""
import io, json, os, re, sys

ROOT = r"D:\MyCode\InfiniTrader_handbook"
DOCS = os.path.join(ROOT, "docs")
API = os.path.join(ROOT, "api")
RAW = os.path.join(ROOT, "_raw")
SITE = "https://infinitrader.quantdo.com.cn/pythongo_v2"

SPLIT_PREFIXES = ("modules/", "examples")
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
ANCHOR_LINE = re.compile(r'^<a id="([^"]+)"></a>$')
HEAD_LINE = re.compile(r"^(#{1,6}) (.+)$")


def safe(name):
    s = name.strip()
    s = s.strip("`")
    s = re.sub(r"\(\)$", "", s)
    s = s.replace("/", "-").replace("\\", "-").replace(":", "-").replace("*", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s or "untitled"


def ascii_name(title, anchor, fallback):
    """文件/目录名优先用英文原名，中文标题改用官方锚点（本身就是英文）"""
    s = safe(title)
    if re.fullmatch(r"[A-Za-z0-9._ -]+", s):
        return s.replace(" ", "-")
    if anchor and re.fullmatch(r"[A-Za-z0-9._-]+", anchor):
        return anchor
    return fallback


def parse_sections(md):
    """返回 (preamble, [{level, title, anchor, body_lines}])，按标题顺序"""
    lines = md.split("\n")
    # 去掉 front matter 与一级标题
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1
    sections, preamble = [], []
    cur = None
    pending_anchor = None
    while i < len(lines):
        ln = lines[i]
        m = ANCHOR_LINE.match(ln.strip())
        if m:
            pending_anchor = m.group(1)
            i += 1
            continue
        h = HEAD_LINE.match(ln.strip())
        if h and len(h.group(1)) >= 2:
            cur = {"level": len(h.group(1)), "title": h.group(2).strip(),
                   "anchor": pending_anchor, "body": []}
            pending_anchor = None
            sections.append(cur)
            i += 1
            continue
        if h and len(h.group(1)) == 1:
            i += 1
            continue
        if cur is None:
            preamble.append(ln)
        else:
            cur["body"].append(ln)
        i += 1
    return "\n".join(preamble).strip(), sections


def relocate(text, src_abs, dst_abs):
    def sub(m):
        label, href = m.group(1), m.group(2)
        if href.startswith(("http://", "https://", "mailto:")):
            return m.group(0)
        path, sep, frag = href.partition("#")
        if not path:
            return m.group(0)
        target = os.path.normpath(os.path.join(os.path.dirname(src_abs), path))
        rel = os.path.relpath(target, os.path.dirname(dst_abs)).replace(os.sep, "/")
        return f"[{label}]({rel}{sep}{frag})"
    return LINK.sub(sub, text)


def summary_of(body):
    for ln in body.split("\n"):
        s = ln.strip()
        if not s or s.startswith(("|", ">", "#", "-", "```", "<a ")):
            continue
        s = re.sub(r"`([^`]*)`", r"\1", s)
        s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
        s = re.sub(r"\*\*|__", "", s)
        return s[:70]
    return ""


def params_line(body):
    """从参数表抽出紧凑签名：fn(a, b, c=default)"""
    lines = body.split("\n")
    for idx, ln in enumerate(lines):
        if ln.strip().startswith("|") and "参数名" in ln:
            header = [c.strip() for c in ln.strip().strip("|").split("|")]
            try:
                i_name = header.index("参数名")
            except ValueError:
                return ""
            try:
                i_def = header.index("默认值")
            except ValueError:
                i_def = -1
            args = []
            j = idx + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                cells = [c.strip() for c in lines[j].strip().strip("|").split("|")]
                if len(cells) > i_name:
                    nm = re.sub(r"`", "", cells[i_name])
                    dv = ""
                    if i_def >= 0 and len(cells) > i_def:
                        dv = re.sub(r"`", "", cells[i_def]).strip()
                    if dv and dv not in ("必填", "-", ""):
                        args.append(f"{nm}={dv}")
                    else:
                        args.append(nm)
                j += 1
            return ", ".join(args)
    return ""


def has_table(body):
    return any(l.strip().startswith("|") for l in body.split("\n"))


def detect_kind(title, body, kids, route):
    t = title.strip().strip("`")
    if t.endswith("()") or "| 参数名 |" in body:
        return "function"
    head = body.strip()[:200]
    if re.search(r"类型：`[^`]+`", head):
        return "attribute"
    if kids:
        return "class"
    if route.startswith("/examples"):
        return "recipe"
    if route.startswith("/modules"):
        if re.fullmatch(r"[A-Za-z_][\w.]*", t):
            return "class"
        if has_table(body):
            return "class"
    return "section"


def module_label(cls, hits, fm_title, route):
    # 文档页本身就是模块页（标题形如 pythongo.core）时以页面为准，最准确
    if re.match(r"^pythongo(\.|$)", fm_title):
        return fm_title
    if hits:
        return hits[0][0]
    if "pythongo_classdef" in route:
        return "pythongo.classdef"
    if "/modules/" in route:
        return "pythongo." + route.strip("/").split("/")[-1].split("pythongo_")[-1]
    return route.strip("/").replace("/", ".")


def main():
    pages = json.load(io.open(os.path.join(RAW, "pages.json"), encoding="utf-8"))
    imports = __import__("importmap").build()
    symbols = []
    count = 0
    for page in pages:
        rel = page["path"]
        if not rel.startswith(SPLIT_PREFIXES):
            continue
        src_abs = os.path.join(DOCS, rel.replace("/", os.sep))
        md = io.open(src_abs, encoding="utf-8").read()
        fm_title = page["title"]
        route = "/" + rel[:-3]
        module = route.strip("/").split("/")[-1]
        if route.startswith("/modules/pythongo_classdef/"):
            module = route.strip("/").split("/")[-1]
        out_dir = os.path.join(API, *route.strip("/").split("/")[:-1])
        os.makedirs(out_dir, exist_ok=True)

        preamble, sections = parse_sections(md)
        h2s = [s for s in sections if s["level"] == 2]
        used = set()

        for n2, h2 in enumerate(h2s):
            cls = ascii_name(h2["title"], h2["anchor"], f"section-{n2 + 1}")
            hits = imports.get(cls) or []
            mod_label = module_label(cls, hits, fm_title, route)
            if hits:
                # 与所在文档页一致的导入写法排在最前
                hits = ([h for h in hits if h[0] == mod_label] +
                        [h for h in hits if h[0] != mod_label])
            imp_line = ""
            if hits:
                imp_line = f"import: \"from {hits[0][0]} import {cls}\"\n"
                if len(hits) > 1:
                    imp_line += "import_alt: \"" + ", ".join(f"from {m} import {cls}" for m, _ in hits[1:]) + "\"\n"
            kids = []
            started = False
            for s in sections:
                if s is h2:
                    started = True
                    continue
                if started:
                    if s["level"] == 2:
                        break
                    if s["level"] == 3:
                        kids.append(s)
            anchor = h2["anchor"]
            body = "\n".join(h2["body"]).strip()
            kind = detect_kind(h2["title"], body, kids, route)
            url = f"{SITE}{route}" + (f"#{anchor}" if anchor else "")
            base_dir = f"api/{route.strip('/')}"
            card_rel = f"{base_dir}/{cls}.md"
            if card_rel in used:
                card_rel = f"{base_dir}/{cls}-2.md"
            used.add(card_rel)
            dst_abs = os.path.join(ROOT, card_rel.replace("/", os.sep))
            os.makedirs(os.path.dirname(dst_abs), exist_ok=True)
            full_rel = os.path.relpath(src_abs, os.path.dirname(dst_abs)).replace(os.sep, "/")
            parts = []
            parts.append(f"---\ntitle: \"{cls}\"\nmodule: \"{mod_label}\"\nkind: \"{kind}\"\n"
                         f"{imp_line}source: \"{url}\"\n---\n")
            parts.append(f"# `{cls}`\n")
            ctx = f"- 模块: `{mod_label}`  ·  整页: [{'/'.join(route.strip('/').split('/'))}]({full_rel}"
            ctx += f"{'#' + anchor if anchor else ''})  ·  [原文]({url})"
            if hits:
                ctx += f"\n- `from {hits[0][0]} import {cls}`"
            parts.append(ctx)
            if body:
                parts.append(relocate(body, src_abs, dst_abs))
            if kids:
                parts.append(f"**成员 {len(kids)} 项**：" + "、".join(
                    f"[{safe(k['title'])}]({cls}.{ascii_name(k['title'], k['anchor'], 'member')}.md)"
                    for k in kids))
            io.open(dst_abs, "w", encoding="utf-8", newline="\n").write(
                "\n\n".join(parts) + "\n")
            count += 1
            symbols.append({
                "name": cls, "kind": kind, "module": mod_label, "scope": "",
                "title": h2["title"].strip("`"),
                "anchor": anchor, "path": card_rel,
                "summary": summary_of(body), "signature": "",
                "imports": [f"from {m} import {cls}" for m, _ in hits],
                "source": url,
            })

            for k in kids:
                mem = ascii_name(k["title"], k["anchor"], "member")
                member = re.sub(r"\(\)$", "", k["title"].strip("`")).strip()
                kbody = "\n".join(k["body"]).strip()
                mkind = detect_kind(k["title"], kbody, [], route)
                if mkind in ("class", "section", "recipe"):
                    mkind = "attribute" if "类型：`" in kbody[:200] else "function"
                kurl = f"{SITE}{route}#{k['anchor']}" if k["anchor"] else f"{SITE}{route}"
                krel = f"{base_dir}/{cls}.{mem}.md"
                kdst = os.path.join(ROOT, krel.replace("/", os.sep))
                os.makedirs(os.path.dirname(kdst), exist_ok=True)
                full_k = os.path.relpath(src_abs, os.path.dirname(kdst)).replace(os.sep, "/")
                p = [f"---\ntitle: \"{cls}.{member}\"\nmodule: \"{mod_label}\"\n"
                     f"kind: \"{mkind}\"\nscope: \"{cls}\"\nsource: \"{kurl}\"\n---\n",
                     f"# `{cls}.{member}`\n",
                     f"- 模块: `{mod_label}` › `{cls}`  ·  [类总览]({cls}.md)  ·  "
                     f"[整页]({full_k}#{k['anchor'] or ''})  ·  [原文]({kurl})"]
                if kbody:
                    p.append(relocate(kbody, src_abs, kdst))
                io.open(kdst, "w", encoding="utf-8", newline="\n").write(
                    "\n\n".join(p) + "\n")
                count += 1
                symbols.append({
                    "name": member, "kind": mkind, "module": mod_label, "scope": cls,
                    "title": k["title"].strip("`"),
                    "anchor": k["anchor"], "path": krel,
                    "summary": summary_of(kbody), "signature": params_line(kbody),
                    "imports": [f"from {m} import {cls}" for m, _ in hits],
                    "source": kurl,
                })

        # 模块索引
        idx_rel = f"api/{route.strip('/')}/_index.md"
        idx_abs = os.path.join(ROOT, idx_rel.replace("/", os.sep))
        os.makedirs(os.path.dirname(idx_abs), exist_ok=True)
        lines = [f"---\ntitle: \"{fm_title}\"\nsection: \"{route.strip('/')}\"\n---\n",
                 f"# {fm_title}\n",
                 f"原文: {SITE}{route}\n",
                 "| 名称 | 类型 | 说明 | 卡片 |",
                 "| --- | --- | --- | --- |"]
        for s in symbols:
            if not s["path"].startswith(base_dir + "/"):
                continue
            label = f"{s['scope']}.{s['name']}" if s["scope"] else s["name"]
            card = os.path.relpath(os.path.join(ROOT, s["path"].replace("/", os.sep)),
                                   os.path.dirname(idx_abs)).replace(os.sep, "/")
            lines.append(f"| `{label}` | {s['kind']} | {s['summary'][:40]} | [打开]({card}) |")
        io.open(idx_abs, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")

    json.dump(symbols, io.open(os.path.join(RAW, "symbols.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("api cards:", count, "symbols:", len(symbols))


if __name__ == "__main__":
    main()
