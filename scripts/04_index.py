# -*- coding: utf-8 -*-
"""07：生成导航与索引：index/pages.md、index/api.md、index/cheatsheet.md、
index/symbols.tsv / symbols.json、根目录 llms.txt"""
import io, json, os, re
from collections import OrderedDict

ROOT = r"D:\MyCode\InfiniTrader_handbook"
RAW = os.path.join(ROOT, "_raw")
IDX = os.path.join(ROOT, "index")
SITE = "https://infinitrader.quantdo.com.cn/pythongo_v2"

GROUP_TITLES = OrderedDict([
    ("tutorial", "教程入门"),
    ("modules", "API 参考（模块）"),
    ("examples", "实用例子"),
    ("styleguide", "代码风格规范"),
    ("backtesting", "回测"),
    ("faq", "常见问题"),
    ("client", "客户端 / 调试"),
    ("changelog", "更新日志"),
    ("other", "其它"),
])


def group_of(route):
    r = route.strip("/").split("/")[0] if route.strip("/") else "other"
    return r if r in GROUP_TITLES else "other"


def main():
    os.makedirs(IDX, exist_ok=True)
    pages = json.load(io.open(os.path.join(RAW, "pages.json"), encoding="utf-8"))
    symbols = json.load(io.open(os.path.join(RAW, "symbols.json"), encoding="utf-8"))

    # ---------- pages.md ----------
    lines = ["# 页面清单（全书 39 页）", "",
             "| 分组 | 页面 | 路由 | 本地文件 |", "| --- | --- | --- | --- |"]
    for g, gtitle in GROUP_TITLES.items():
        for p in pages:
            if group_of(p["route"]) != g:
                continue
            lines.append(f"| {gtitle} | {p['title']} | `{p['route']}` | "
                         f"[{p['path']}](../docs/{p['path']}) |")
    io.open(os.path.join(IDX, "pages.md"), "w", encoding="utf-8", newline="\n").write(
        "\n".join(lines) + "\n")

    # ---------- api.md ----------
    by_mod = OrderedDict()
    for s in symbols:
        by_mod.setdefault(s["module"], []).append(s)
    kind_rank = {"class": 0, "function": 1, "attribute": 2, "recipe": 3, "section": 4}
    lines = ["# API 总览（177 张速查卡）", "",
             "> 用法：先在本表按名字/说明定位，再打开对应卡片（每张只有几百字，比整页省 token）。",
             ""]
    for mod in sorted(by_mod):
        items = sorted(by_mod[mod], key=lambda s: (kind_rank.get(s["kind"], 9), s["scope"], s["name"]))
        lines.append(f"## {mod}")
        lines.append("")
        lines.append("| 符号 | 类型 | 签名 | 说明 | 卡片 |")
        lines.append("| --- | --- | --- | --- | --- |")
        for s in items:
            label = f"{s['scope']}.{s['name']}" if s["scope"] else s["name"]
            if s["kind"] == "function":
                sig = f"{label}({s['signature']})" if s["signature"] else f"{label}()"
            elif s["kind"] == "class":
                sig = f"class {s['name']}"
            elif s["kind"] == "attribute":
                sig = "属性"
            else:
                sig = "—"
            sig = sig.replace("|", "\\|")
            summ = (s["summary"] or "").replace("|", "\\|")
            card = os.path.relpath(os.path.join(ROOT, s["path"].replace("/", os.sep)),
                                   os.path.dirname(os.path.join(IDX, "api.md"))).replace(os.sep, "/")
            lines.append(f"| `{label}` | {s['kind']} | `{sig}` | {summ} | [卡片]({card}) |")
        lines.append("")
    io.open(os.path.join(IDX, "api.md"), "w", encoding="utf-8", newline="\n").write(
        "\n".join(lines) + "\n")

    # ---------- cheatsheet.md ----------
    lines = ["# 速查表（一行一个 API，只有签名）", "",
             "> 需要参数含义/返回类型时再打开 `index/api.md` 或对应卡片。", ""]
    for mod in sorted(by_mod):
        items = [s for s in by_mod[mod] if s["kind"] in ("class", "function", "attribute")]
        if not items:
            continue
        lines.append(f"## {mod}")
        lines.append("")
        lines.append("```python")
        for kind in ("class", "function", "attribute"):
            for s in items:
                if s["kind"] != kind:
                    continue
                label = f"{s['scope']}.{s['name']}" if s["scope"] else s["name"]
                if kind == "class":
                    lines.append(f"class {s['name']}")
                elif kind == "attribute":
                    lines.append(f"{label}  # 属性")
                elif s["signature"]:
                    lines.append(f"{label}({s['signature']})")
                else:
                    lines.append(f"{label}()")
        lines.append("```")
        lines.append("")
    io.open(os.path.join(IDX, "cheatsheet.md"), "w", encoding="utf-8", newline="\n").write(
        "\n".join(lines) + "\n")

    # ---------- symbols.tsv / json ----------
    rows = ["name\tkind\tmodule\tscope\tsignature\tsummary\tpath"]
    for s in sorted(symbols, key=lambda x: (x["module"], x["scope"], x["name"])):
        rows.append("\t".join([s["name"], s["kind"], s["module"], s["scope"],
                               s["signature"], s["summary"], s["path"]]))
    io.open(os.path.join(IDX, "symbols.tsv"), "w", encoding="utf-8", newline="\n").write(
        "\n".join(rows) + "\n")
    json.dump(symbols, io.open(os.path.join(IDX, "symbols.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    # ---------- llms.txt ----------
    lines = ["# PythonGO v2 开发手册（本地镜像）", "",
             "> 无限易 PythonGO v2 官方文档的离线 Markdown 版，按 API 拆分，便于检索与低 token 阅读。",
             "> 原始站点: " + SITE, "",
             "## 索引",
             "- [index/api.md](index/api.md): 全部 API（含签名、说明、卡片链接）",
             "- [index/cheatsheet.md](index/cheatsheet.md): 全部签名速查",
             "- [index/pages.md](index/pages.md): 全部页面清单",
             "- [index/symbols.tsv](index/symbols.tsv): 机器可读符号表", ""]
    for p in pages:
        lines.append(f"- [{p['title']}](docs/{p['path']})")
    io.open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8", newline="\n").write(
        "\n".join(lines) + "\n")

    print("pages:", len(pages), "symbols:", len(symbols), "modules:", len(by_mod))


if __name__ == "__main__":
    main()
