# -*- coding: utf-8 -*-
"""从 docs 的代码块里提取 import 关系：符号名 -> 模块路径（取出现次数最多者）"""
import glob, io, os, re
from collections import defaultdict, Counter

ROOT = r"D:\MyCode\InfiniTrader_handbook"
FENCE = re.compile(r"```[a-zA-Z]*\n(.*?)```", re.S)
FROM = re.compile(r"^\s*from\s+([A-Za-z_][\w.]*)\s+import\s+(.+)$")
IMP = re.compile(r"^\s*import\s+([A-Za-z_][\w.]*)\s*$")


def build(root=ROOT):
    votes = defaultdict(Counter)
    for p in glob.glob(os.path.join(root, "docs", "**", "*.md"), recursive=True):
        text = io.open(p, encoding="utf-8").read()
        for block in FENCE.findall(text):
            for line in block.splitlines():
                if line.lstrip().startswith("#"):
                    continue
                m = FROM.match(line)
                if m:
                    mod = m.group(1)
                    names = [n.strip().split(" as ")[0].strip()
                             for n in m.group(2).replace("(", " ").replace(")", " ").split(",")]
                    for n in names:
                        if re.fullmatch(r"[A-Za-z_]\w*", n):
                            votes[n][mod] += 1
                    continue
                m = IMP.match(line)
                if m:
                    mod = m.group(1)
                    votes[mod.split(".")[-1]][mod] += 1
    return {k: v.most_common() for k, v in votes.items()}


def primary_map(root=ROOT):
    return {k: v[0][0] for k, v in build(root).items()}


if __name__ == "__main__":
    for k, v in sorted(build().items()):
        print(f"{k:24s} " + ", ".join(f"{m}({c})" for m, c in v))
    print("total", len(build()))
