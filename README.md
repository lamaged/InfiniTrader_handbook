# PythonGO v2 本地手册

无限易 PythonGO v2 官方文档（<https://infinitrader.quantdo.com.cn/pythongo_v2/>）的**离线 Markdown 镜像 + 按 API 拆分的速查卡**。
目的是：查一个调用、一个参数时，只读几百字，而不是拿整页网页喂给 AI。

- 站点点数：39 个页面，抓取于 **2026-11-20**
- 体积对比：原始 HTML 合计 **4.7 MB** → 整页 Markdown `docs/` 只有 **157 KB**（约 1/30）
- 拆成 **177 张 API 速查卡**在 `api/`，平均 **0.86 KB/张**（最大 6 KB 是一整段示例代码）
- 单页网页（HTML）通常 50–400 KB，转成 Markdown 后 1–10 KB；单张速查卡 0.3–1 KB

---

## 1. 目录结构

```
InfiniTrader_handbook/
├─ README.md           ← 本文件
├─ CLAUDE.md           ← 给 Claude Code 的规矩（Claude Code 会自动读）
├─ AGENTS.md           ← 给其它 AI 编码工具（Codex / DeepSeek 等）的规矩
├─ llms.txt            ← 站点索引（llms.txt 约定格式）
├─ docs/               ← 官方文档的整页 Markdown 镜像（按章节分文件）
│  ├─ index.md                    首页
│  ├─ tutorial/                   教程：quick_start / first_strategy / second_strategy / how_it_works
│  ├─ modules/                    API 参考：pythongo_core / base / utils / indicator / option / ui / types …
│  ├─ examples.md                 实用例子
│  ├─ styleguide/                 代码风格与策略规范
│  ├─ backtesting/                回测
│  ├─ faq/                       安装、常见问题、v1→v2 字段映射
│  └─ changelog.md 等
├─ api/                ← 按「一条 API 一个文件」拆出来的速查卡
│  ├─ modules/pythongo_core/MarketCenter.get_kline_data.md
│  ├─ modules/pythongo_base/BaseStrategy.on_init.md
│  └─ <模块>/_index.md            该模块的符号总表
├─ index/              ← 索引
│  ├─ pages.md                    39 个页面清单（分组）
│  ├─ api.md                      177 个 API 一览（签名 + 说明 + 卡片链接）
│  ├─ cheatsheet.md               只含签名，最省 token 的全景表
│  ├─ symbols.tsv / symbols.json  机器可读符号表
├─ assets/img/         ← 文档里的截图（已本地化，离线可看）
├─ tools/q.py          ← 检索工具（全文 / 符号 / 模块 / 卡片）
├─ scripts/            ← 抓取与转换流水线 + update.ps1
└─ _raw/               ← 原始 HTML 缓存（重建用，可删）
```

## 2. 三种用法

### A. 人看：VS Code 里当书读

- 打开 `README.md`，按 `Ctrl+Shift+V` 预览；侧边栏「大纲」可直接跳章节。
- 想按目录读 → `index/pages.md`；想按 API 读 → `index/api.md`。
- 图片、锚点、跨页链接都是本地相对路径，断网也能用。

### B. 命令行查：`tools/q.py`

```powershell
python tools\q.py 订阅行情                     # 全书全文检索，返回 文件: 命中行
python tools\q.py --sym get_kline_data         # 查符号：签名 / 说明 / 卡片路径
python tools\q.py --sym get_kline_data --show  # 直接打印这张速查卡
python tools\q.py --cat pythongo.utils         # 列出该模块所有 API
python tools\q.py --pages                      # 列出全部页面
python tools\q.py --sheets                     # 列出全部速查卡
```

### C. 给 AI 用（重点）

把本目录放在策略工程旁边（或直接用 VS Code 把两个文件夹加入同一个工作区），然后在对话里这样使唤：

```text
先看 InfiniTrader_handbook/index/cheatsheet.md，找出订阅行情的 API，
再打开对应速查卡，给我一个 on_start 里订阅 ag2602 并打印 tick 的例子。
```

AI 的读取顺序被 `CLAUDE.md` / `AGENTS.md` 约束为
**速查表 → 符号表 → 单张卡片 →（必要时）整页**，正常一次提问只会读 1–3 个几百字的文件。

实测：问「get_kline_data 的参数和返回」这种问题，
以前把整页 HTML 丢进上下文平均约 3 万 token（大页面接近 10 万）；
现在读 `index/cheatsheet.md` 里一行 + 一张卡片 ≈ 400 token。

## 3. 为什么这样组织（设计取舍）

| 做法 | 为什么 |
| --- | --- |
| 先存原始 HTML（`_raw/`），再转换 | 官方改版时只重跑转换、不重抓；出问题能对照原文 |
| 整页 Markdown 按「官方章节」保留（`docs/`） | 教程、规范、FAQ 是有前后文的，拆碎反而看不懂 |
| API 参考再拆成「一条一个文件」（`api/`） | 你痛点是「查一个调用要翻整页」；一张卡 300–800 字，读它就够 |
| 三套索引（速查表 / 总览表 / TSV） | 给人看、给 AI 看、给 grep 用，三种粒度；AI 先 grep 再读，避免整篇塞进上下文 |
| 保留官方锚点 + 相对链接 | 本地也能 `文件.md#锚点` 精确引用，AI 回答时可溯源 |
| `CLAUDE.md` / `AGENTS.md` 写死检索顺序 | 光有文件不够，得约束 AI「先索引、后正文、一次只读一张卡」 |
| 一条命令重建 | 文档会变；`update.ps1` 让「更新」成本降到一次回车 |

## 4. 更新（官方文档变了怎么办）

```powershell
cd D:\MyCode\InfiniTrader_handbook
powershell -ExecutionPolicy Bypass -File scripts\update.ps1           # 增量：只补新页面
powershell -ExecutionPolicy Bypass -File scripts\update.ps1 -Force    # 全量：重新抓所有页面
```

（脚本存成 UTF-8 with BOM，Windows PowerShell 5.1 才认中文；中途每步失败会直接停下。）

流水线：`01_fetch`（抓 HTML）→ `02_docs`（转 Markdown）→ `03_api`（拆卡片）→ `04_index`（建索引）→ `05_check`（校验链接与锚点，有问题会报错退出）。

想额外确认「有没有整段内容被漏掉」，可跑一次完整性抽检（逐句比对 HTML 原文与生成的 Markdown）：

```powershell
python scripts\06_fidelity.py     # 输出「漏了几段」；当前 39/39 页为 0 缺失
```

转换规则要点（`scripts/mdconv.py`）：

- 正文取 Nextra 的 `article > main`，丢掉面包屑/上一页下一页/锚点图标；
- 代码块保留语言与缩进（`pre[data-language]` → ```python），带文件名的代码块输出 `**`文件名`**`；
- HeroUI 表格 → Markdown 表格；Nextra callout → `> [!NOTE] / [!WARNING]`；可折叠目录树 → ```text 缩进树；
- 中文标题的锚点取官方 `<a class="subheading-anchor" id>`，所以站内 `#锚点` 链接在本地仍然有效；
- 站点自身的断链（如 `#klineproducer` 实际是 `kline-producer`）会自动按归一化锚点名修正；
- 文档里的截图下载到 `assets/img/`，链接改成本地相对路径（离线可看）。

## 5. 兼容性 / 注意

- 手册内容版权归无限易（QuantDo）所有，本目录仅供本地开发查阅。
- 若站点改版（Next.js buildId 变化没关系，脚本会自动定位），转换规则可能需要微调：
  先跑 `05_check.py` 看报错，再检查 `_raw/pages/*.html` 的结构。
- `_raw/` 只用于重建，已被 `.gitignore` 忽略；删了也不影响阅读，下次 `update.ps1 -Force` 会重新下载。
- `.vscode/settings.json` 已把 `_raw/` 排除在搜索与文件监视之外，所以 VS Code 全局搜索只会命中手册正文。
