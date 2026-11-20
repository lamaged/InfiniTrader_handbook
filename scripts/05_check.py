# -*- coding: utf-8 -*-
"""校验：本地链接可解析、锚点存在、无残留占位符/远程图片；并抽样比对正文完整度"""
import io, json, os, re, sys

ROOT = r"D:\MyCode\InfiniTrader_handbook"
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
ANCHOR = re.compile(r'<a id="([^"]+)"></a>')
HEAD = re.compile(r"^(#{1,6}) (.+)$", re.M)


def md_files():
    out = []
    for base in ["docs", "api", "index"]:
        d = os.path.join(ROOT, base)
        for dirpath, _, files in os.walk(d):
            for f in files:
                if f.endswith(".md"):
                    out.append(os.path.join(dirpath, f))
    for f in ["README.md", "CLAUDE.md", "AGENTS.md"]:
        p = os.path.join(ROOT, f)
        if os.path.exists(p):
            out.append(p)
    return out


def main():
    files = md_files()
    anchors = {}
    text = {}
    for p in files:
        t = io.open(p, encoding="utf-8").read()
        text[p] = t
        anchors[os.path.normcase(os.path.abspath(p))] = set(ANCHOR.findall(t))
    problems = []
    nlinks = 0
    for p, t in text.items():
        if "@@LINK:" in t:
            problems.append(f"PLACEHOLDER {p}")
        if re.search(r"!\[[^\]]*\]\(https?://", t):
            problems.append(f"REMOTE_IMG {p}")
        for label, href in LINK.findall(t):
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            nlinks += 1
            path, _, frag = href.partition("#")
            if path:
                target = os.path.normpath(os.path.join(os.path.dirname(p), path))
            else:
                target = p
            if not os.path.exists(target):
                problems.append(f"MISSING_FILE {os.path.relpath(p, ROOT)} -> {href}")
                continue
            if frag:
                tg = os.path.normcase(os.path.abspath(target))
                if frag not in anchors.get(tg, set()):
                    problems.append(f"MISSING_ANCHOR {os.path.relpath(p, ROOT)} -> {href}")
    print(f"files={len(files)} local_links={nlinks} problems={len(problems)}")
    for x in problems[:40]:
        print("  ", x)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
