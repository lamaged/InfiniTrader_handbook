# -*- coding: utf-8 -*-
"""PythonGO 手册本地检索工具（省 token 用）

用法：
  python tools/q.py 订阅行情              # 全书全文检索（默认返回命中行，最多 12 条）
  python tools/q.py --sym get_kline_data  # 查符号：签名 + 说明 + 卡片路径
  python tools/q.py --sym get_kline_data --show   # 直接打印该 API 的完整速查卡
  python tools/q.py --cat pythongo.utils  # 列出某模块的所有 API
  python tools/q.py --pages               # 列出全部页面
  python tools/q.py --sheets              # 列出所有速查卡（一行一个）
选项：
  -n N      全文检索返回条数（默认 12）
  --full    不截断命中行
"""
import argparse, io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV = os.path.join(ROOT, "index", "symbols.tsv")
CTX = 90

try:  # 统一用 UTF-8 输出，避免 Windows 控制台编码把中文写坏
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def out(s=""):
    try:
        sys.stdout.write(s + "\n")
    except UnicodeEncodeError:
        sys.stdout.write(s.encode("ascii", "replace").decode("ascii") + "\n")


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def load_symbols():
    rows = []
    with io.open(TSV, encoding="utf-8") as f:
        head = f.readline()
        for line in f:
            c = line.rstrip("\n").split("\t")
            if len(c) >= 7:
                rows.append(dict(zip(["name", "kind", "module", "scope", "signature",
                                      "summary", "path"], c)))
    return rows


def md_files(dirs=("docs", "api", "index")):
    for d in dirs:
        for dp, _, fs in os.walk(os.path.join(ROOT, d)):
            for fn in fs:
                if fn.endswith(".md"):
                    yield os.path.join(dp, fn)


def search(kw, limit, full):
    pats = [k.lower() for k in kw]
    hits = 0
    for p in md_files():
        text = io.open(p, encoding="utf-8").read()
        title = re.search(r"^# (.+)$", text, re.M)
        for ln in text.splitlines():
            low = ln.lower()
            if all(x in low for x in pats):
                s = ln.strip()
                if s.startswith("<a id"):
                    continue
                if not full and len(s) > CTX:
                    s = s[:CTX] + "…"
                out(f"{rel(p)}: {s}")
                hits += 1
                if hits >= limit:
                    out(f"... (已达 {limit} 条上限，可加 -n 扩大)")
                    return
        del title
    if hits == 0:
        out("(无命中)")


def find_symbol(rows, name):
    n = name.lower()
    exact = [r for r in rows if r["name"].lower() == n]
    if exact:
        return exact
    exact = [r for r in rows if f"{r['scope']}.{r['name']}".lower() == n]
    if exact:
        return exact
    return [r for r in rows if n in r["name"].lower() or n in r["scope"].lower()]


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("query", nargs="*", help="全文检索关键词")
    ap.add_argument("--sym", help="按符号名查 API")
    ap.add_argument("--show", action="store_true", help="打印速查卡全文")
    ap.add_argument("--cat", help="列出模块下所有 API")
    ap.add_argument("--pages", action="store_true", help="列出全部页面")
    ap.add_argument("--sheets", action="store_true", help="列出全部速查卡")
    ap.add_argument("-n", type=int, default=12)
    ap.add_argument("--full", action="store_true")
    a = ap.parse_args()

    rows = load_symbols()

    if a.pages:
        for p in sorted(md_files(("docs",))):
            t = io.open(p, encoding="utf-8").read()
            m = re.search(r"^title: \"(.+)\"$", t, re.M)
            out(f"{rel(p):60s} {m.group(1) if m else ''}")
        return
    if a.sheets:
        for r in sorted(rows, key=lambda x: (x["module"], x["scope"], x["name"])):
            label = f"{r['scope']}.{r['name']}" if r["scope"] else r["name"]
            out(f"{label:36s} {r['path']}")
        return
    if a.cat:
        c = a.cat.lower()
        sel = [r for r in rows if c in r["module"].lower() or c in r["path"].lower()]
        for r in sorted(sel, key=lambda x: (x["scope"], x["name"])):
            label = f"{r['scope']}.{r['name']}" if r["scope"] else r["name"]
            out(f"{label:36s} {(r['signature'] or '')[:70]:70s} {r['path']}")
        out(f"({len(sel)} 项)")
        return
    if a.sym:
        hits = find_symbol(rows, a.sym)
        if not hits:
            out("(未找到该符号，试试全文检索)")
            return
        for r in hits[:8]:
            label = f"{r['scope']}.{r['name']}" if r["scope"] else r["name"]
            out(f"{label}  [{r['kind']}]  模块 {r['module']}")
            if r["signature"]:
                out(f"  签名: {label}({r['signature']})")
            if r["summary"]:
                out(f"  说明: {r['summary']}")
            out(f"  卡片: {r['path']}")
            if a.show and len(hits) == 1:
                out("-" * 60)
                out(io.open(os.path.join(ROOT, r["path"]), encoding="utf-8").read())
        return
    if a.query:
        search(a.query, a.n, a.full)
        return
    out(__doc__)


if __name__ == "__main__":
    main()
