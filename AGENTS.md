# AGENTS.md — 给其它 AI 编码工具（Codex / DeepSeek / 通义等）

本仓库是 **无限易 PythonGO v2 官方文档的离线镜像**。查接口、查参数、查回调，
一律读本地文件，**不要**再访问 `https://infinitrader.quantdo.com.cn/pythongo_v2/`。

完整使用规则见 [CLAUDE.md](CLAUDE.md)（内容与本文一致，Claude Code 会自动加载它）。
关键三条：

1. **先索引后正文**：`index/cheatsheet.md`（全部签名）→ `grep index/symbols.tsv` →
   打开 `api/<模块>/<类>.<成员>.md` 那一张卡；只有需要背景/完整示例时才读 `docs/`。
2. **一次只读一个卡片**（0.3–1 KB），禁止把 `api/`、`docs/`、`index/api.md` 整篇塞进上下文。
3. 引用时给出 `api/...md` 或 `docs/....md#锚点` 路径。

命令行检索（可选）：

```powershell
python tools\q.py 订阅行情                     # 全书全文检索
python tools\q.py --sym get_kline_data --show  # 打印单张速查卡
python tools\q.py --cat pythongo.utils         # 列模块内所有 API
```

内容更新：`powershell -ExecutionPolicy Bypass -File scripts\update.ps1`（官方文档变了才需要）。
