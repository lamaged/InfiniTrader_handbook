# -*- coding: utf-8 -*-
"""把转换阶段的占位链接 + 远程图片解析成最终 Markdown：
  @@LINK:route#anchor@@  ->  相对当前文件的 docs/ 路径
  ![](https://...png)    ->  assets/img/xxx.png 本地文件
"""
import io, json, os, re, urllib.request

SITE = "https://infinitrader.quantdo.com.cn/pythongo_v2"
LINK_RE = re.compile(r"\[([^\]]*)\]\(@@LINK:([^@]*)@@\)")
IMG_RE = re.compile(r"!\[([^\]]*)\]\((https?://[^)\s]+)\)")


class Renderer:
    def __init__(self, root, anchor_map, page_paths=None, page_anchors=None):
        self.root = root
        self.docs = os.path.join(root, "docs")
        self.assets = os.path.join(root, "assets", "img")
        os.makedirs(self.assets, exist_ok=True)
        # route#anchor -> docs 相对路径
        self.anchor_map = anchor_map
        self.page_map = dict(page_paths or {})
        for key, path in anchor_map.items():
            route = key.split("#", 1)[0]
            self.page_map.setdefault(route, path)
        self.page_anchors = page_anchors or {}
        self.norm_anchors = {}
        for path, anchors in self.page_anchors.items():
            for a in anchors:
                self.norm_anchors[(path, re.sub(r"[^a-z0-9_]", "", a.lower()))] = a
        self.img_done = {}
        self.missing = set()
        self.fixed = set()

    # ---------- 链接 ----------
    def resolve_link(self, route, frag, out_abs):
        if not route:  # 同页锚点
            base = self.cur_route or "/"
            target = self.anchor_map.get(f"{base}#{frag}")
            if target:
                rel = os.path.relpath(os.path.join(self.docs, target.replace("/", os.sep)),
                                      os.path.dirname(out_abs))
                return rel.replace(os.sep, "/") + "#" + frag
            return "#" + frag
        route = route or "/"
        key = f"{route}#{frag}" if frag else None
        target = self.anchor_map.get(key) if key else self.page_map.get(route)
        if not target:
            target = self.page_map.get(route)
        if not target:
            self.missing.add(f"{route}#{frag}")
            return SITE + ("" if route == "/" else route) + (("#" + frag) if frag else "")
        if frag:
            frag = self.fix_frag(target, frag)
        rel = os.path.relpath(os.path.join(self.docs, target.replace("/", os.sep)),
                              os.path.dirname(out_abs))
        rel = rel.replace(os.sep, "/")
        if frag:
            rel += "#" + frag
        return rel

    def fix_frag(self, target, frag):
        """站点自身偶有断链，按归一化锚点名兜底修正"""
        anchors = self.page_anchors.get(target)
        if anchors is None or not anchors or frag in anchors:
            return frag
        alt = self.norm_anchors.get((target, re.sub(r"[^a-z0-9_]", "", frag.lower())))
        if alt:
            self.fixed.add((target, frag, alt))
            return alt
        return frag
    # ---------- 图片 ----------
    def local_image(self, url, out_abs):
        if url not in self.img_done:
            name = url.split("?")[0].rstrip("/").split("/")[-1] or "img"
            if not re.search(r"\.(png|jpg|jpeg|gif|webp|svg)$", name, re.I):
                name += ".png"
            dst = os.path.join(self.assets, name)
            if not os.path.exists(dst) or os.path.getsize(dst) == 0:
                try:
                    req = urllib.request.Request(url, headers={"User-Agent": "handbook-mirror/1.0"})
                    with urllib.request.urlopen(req, timeout=40) as r:
                        data = r.read()
                    with open(dst, "wb") as f:
                        f.write(data)
                except Exception as e:
                    print("  IMG FAIL", url, e)
                    self.img_done[url] = url
                    return url
            self.img_done[url] = dst
        dst = self.img_done[url]
        if dst.startswith("http"):
            return dst
        rel = os.path.relpath(dst, os.path.dirname(out_abs)).replace(os.sep, "/")
        return rel

    def finalize(self, text, out_rel, cur_route=None):
        """out_rel 相对 root，例如 docs/modules/pythongo_core.md"""
        out_abs = os.path.join(self.root, out_rel.replace("/", os.sep))
        self.cur_route = cur_route
        text = LINK_RE.sub(lambda m: f"[{m.group(1)}]({self.resolve_link_placeholder(m.group(2), out_abs)})", text)

        def img_sub(m):
            alt, url = m.group(1), m.group(2)
            return f"![{alt}]({self.local_image(url, out_abs)})"
        text = IMG_RE.sub(img_sub, text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text

    def resolve_link_placeholder(self, spec, out_abs):
        route, _, frag = spec.partition("#")
        return self.resolve_link(route if route != "" else None, frag, out_abs)
