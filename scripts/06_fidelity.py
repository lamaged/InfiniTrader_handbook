# -*- coding: utf-8 -*-
"""完整性抽检：把每页 HTML 正文和生成的 Markdown 去格式后逐句比对，报告漏掉的句子"""
import io, json, os, re, sys
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "_raw")
PAGES = os.path.join(RAW, "pages")
DOCS = os.path.join(ROOT, "docs")


def norm(s):
    s = s.replace("\u200b", "").replace("\xa0", " ")
    s = s.replace("(opens in a new tab)", "").replace("(opensinanewtab)", "")
    s = re.sub(r"\s+", "", s)
    # 两侧统一抹掉 Markdown 记号与括号，避免 `code()`、**bold** 影响比对
    s = re.sub(r"[`*_>|#\[\]()\\\-├└│─]", "", s)
    return s


def html_sentences(path):
    soup = BeautifulSoup(io.open(path, encoding="utf-8").read(), "lxml")
    main = soup.select_one("article main") or soup.select_one("main")
    for sel in ["div.nextra-breadcrumb"]:
        for d in main.select(sel):
            d.decompose()
    # 去掉上一页/下一页
    for d in main.find_all("div"):
        cls = set(d.get("class") or [])
        if "nx-border-t" in cls and "nx-mb-8" in cls:
            d.decompose()
    out = []
    for p in main.find_all(["p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "td", "th"]):
        t = norm(p.get_text())
        if len(t) >= 8:
            out.append(t)
    for pre in main.find_all("pre"):
        t = norm(pre.get_text())
        if t:
            out.append(t)
    return out


def md_text(path):
    t = io.open(path, encoding="utf-8").read()
    t = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)
    # 链接/图片语法先还原成纯文本，再去掉 Markdown 记号
    t = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    return norm(t)


def main():
    pages = json.load(io.open(os.path.join(RAW, "pages.json"), encoding="utf-8"))
    routes = {r["route"]: r["file"] for r in
              json.load(io.open(os.path.join(RAW, "routes.json"), encoding="utf-8"))}
    bad = 0
    for p in pages:
        html_path = os.path.join(PAGES, routes[p["route"]])
        md_path = os.path.join(DOCS, p["path"].replace("/", os.sep))
        body = md_text(md_path)
        missing = [s for s in html_sentences(html_path) if s not in body]
        if missing:
            bad += 1
            print(f"\n[{p['route']}] 漏 {len(missing)} 段:")
            for s in missing[:5]:
                print("   -", s[:80])
    print(f"\n页面数={len(pages)} 有缺失的页面={bad}")


if __name__ == "__main__":
    main()
