# -*- coding: utf-8 -*-
"""05：把 _raw/pages/*.html 转成 docs/**.md（整页镜像），并产出 _raw/anchor_map.json"""
import io, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bs4 import BeautifulSoup

ROOT = r"D:\MyCode\InfiniTrader_handbook"
RAW = os.path.join(ROOT, "_raw")
PAGES = os.path.join(RAW, "pages")
DOCS = os.path.join(ROOT, "docs")
SITE = "https://infinitrader.quantdo.com.cn/pythongo_v2"


def norm(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


def md_path(route):
    """路由 -> docs 目录下的相对路径"""
    if route == "/":
        return "index.md"
    return route.strip("/") + ".md"


def page_blocks(html_path, route, anchors_map):
    soup = BeautifulSoup(io.open(html_path, encoding="utf-8").read(), "lxml")
    main = soup.select_one("article main") or soup.select_one("main")
    conv_cls = __import__("mdconv").Converter
    conv = conv_cls(route, "", anchors_map)
    blocks = [b for b in conv.blocks(main) if b and str(b).strip()]
    return blocks


def assign_anchors(main, entries=None):
    """标题锚点直接取自 Nextra 的 <a class="subheading-anchor" id="...">"""
    out = {}
    for h in main.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        a = h.select_one("a.subheading-anchor")
        if a is not None and a.get("id"):
            out[id(h)] = a.get("id")
    return out


def main():
    routes = json.load(io.open(os.path.join(RAW, "routes.json"), encoding="utf-8"))
    data = json.load(io.open(os.path.join(RAW, "nextra-data.json"), encoding="utf-8"))
    anchor_map = {}
    pages = []
    page_anchors = {}
    for item in routes:
        route = item["route"]
        html_path = os.path.join(PAGES, item["file"])
        title = (data.get(route) or {}).get("title") or route
        soup = BeautifulSoup(io.open(html_path, encoding="utf-8").read(), "lxml")
        main_el = soup.select_one("article main") or soup.select_one("main")
        amap = assign_anchors(main_el)
        rel = md_path(route)
        page_anchors[rel] = set(amap.values())
        for h_id, anchor in amap.items():
            anchor_map[f"{route}#{anchor}"] = rel
        pages.append((route, title, rel, html_path, amap, main_el))

    from render import Renderer
    rnd = Renderer(ROOT, anchor_map, {r: rel for r, _, rel, _, _, _ in pages}, page_anchors)
    stats = []
    for route, title, rel, html_path, amap, main_el in pages:
        conv = __import__("mdconv").Converter(route, title, amap)
        blocks = [b for b in conv.blocks(main_el) if b and str(b).strip()]
        url = SITE + ("/" if route == "/" else route)
        body = rnd.finalize("\n\n".join(blocks), "docs/" + rel, cur_route=route)
        head = "" if re.match(r"^# ", body) else f"# {title}\n\n"
        text = (f"---\ntitle: \"{title}\"\nurl: \"{url}\"\n---\n\n"
                f"{head}{body}\n")
        dst = os.path.join(DOCS, rel.replace("/", os.sep))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        io.open(dst, "w", encoding="utf-8", newline="\n").write(text)
        stats.append((route, title, len(text), len(blocks), len(amap), rel))
    json.dump(anchor_map, io.open(os.path.join(RAW, "anchor_map.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump([{"route": r, "title": t, "path": rel} for r, t, _, _, _, rel in stats],
              io.open(os.path.join(RAW, "pages.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    stats.sort(key=lambda x: -x[2])
    for r, t, n, b, a, rel in stats:
        print(f"{n:7d}  blocks={b:4d} anchors={a:3d}  {rel}  [{t}]")
    print("TOTAL chars:", sum(s[2] for s in stats))
    print("IMAGES:", len(rnd.img_done), " MISSING LINKS:", sorted(rnd.missing)[:10])
    print("FIXED ANCHORS:", sorted(rnd.fixed))


if __name__ == "__main__":
    main()
