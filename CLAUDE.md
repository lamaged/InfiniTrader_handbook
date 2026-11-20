# PythonGO v2 手册使用规则（给 AI 编码助手）

你在一个包含「无限易 PythonGO v2 官方文档离线镜像」的仓库里工作。
查文档时**必须用本地文件**，不要访问 `infinitrader.quantdo.com.cn`（慢、费 token、还可能被限流）。

## 目录速览

| 路径 | 内容 | 大小 |
| --- | --- | --- |
| `index/cheatsheet.md` | 全部 API 的签名，一行一个 | ~6 KB |
| `index/api.md` | 全部 API：签名 + 一句话说明 + 卡片链接 | ~31 KB |
| `index/symbols.tsv` | 机器可读：name/kind/module/scope/signature/summary/path | 可 grep |
| `index/pages.md` | 39 个页面清单 | ~5 KB |
| `api/<模块>/<类>.<成员>.md` | **单条 API 速查卡**（参数表/返回/注意事项） | 0.3–1 KB |
| `docs/<章节>.md` | 官方整页正文（教程、规范、FAQ、例子） | 1–11 KB |

## 查文档的标准顺序（别跳步，越往后越贵）

1. **知道名字** → `grep "^get_kline_data\b" index/symbols.tsv`（或 `python tools/q.py --sym get_kline_data`），拿到卡片路径。
2. **只知道要做什么**（"怎么订阅行情"/"怎么画线图"）→ 先看 `index/cheatsheet.md` 或 `grep` `index/api.md`。
3. **打开那一张卡片**读参数与返回。
4. 只有需要背景说明/完整示例时，才读 `docs/` 对应整页；教程类问题直接读 `docs/tutorial/*.md`。
5. 命令行检索：`python tools/q.py 关键词`、`python tools/q.py --cat pythongo.utils`。

**不要**为了一个问题把 `api/` 或 `docs/` 整个目录读一遍，也不要一次读 `index/api.md` 全文——
先 grep，再读命中项。

## 回答时的引用

用相对路径 + 锚点，例如：

```text
参数见 api/modules/pythongo_core/MarketCenter.get_kline_data.md
或 docs/modules/pythongo_core.md#get_kline_data
```

## PythonGO 常识（避免常见错）

- 策略有两个模板类：`pythongo.base.BaseStrategy`（不需要 K 线图时用）和 `pythongo.ui.BaseStrategy`（需要 K 线图时用）；
  参数/状态映射用 `from pythongo.base import BaseParams, BaseState, Field`。
- 回调命名：`on_init` / `on_start` / `on_stop` / `on_tick` / `on_order` / `on_trade` / `on_position` / `on_kline` …详见 `docs/modules/pythongo_base.md`。
- 数据类：`KLineData` / `TickData` / `OrderData` 等来自 `pythongo.classdef`。
- 部分 `pythongo.core.MarketCenter` 接口**有调用频率限制，违规会封 IP**；写示例时要提醒用户缓存/节流（卡片里的 `[!WARNING]` 就是这类提示）。
- 代码风格遵循 `docs/styleguide/*.md`（导入顺序、类型注释、异常处理、docstring）。

## 手册本身

- 生成于 2026-11-20，来源见每个文件 front matter 的 `source` / `url`。
- 文档可能过期：若你发现本地缺失某接口，告诉用户运行 `powershell -ExecutionPolicy Bypass -File scripts\update.ps1 -Force` 更新，不要自己抓网页。
