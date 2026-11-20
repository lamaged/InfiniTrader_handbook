---
title: "KLineData"
module: "pythongo.classdef"
kind: "class"
import: "from pythongo.classdef import KLineData"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_classdef/kline#klinedata"
---


# `KLineData`


- 模块: `pythongo.classdef`  ·  整页: [modules/pythongo_classdef/kline](../../../../docs/modules/pythongo_classdef/kline.md#klinedata)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_classdef/kline#klinedata)
- `from pythongo.classdef import KLineData`

K 线数据类

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| `exchange` | `str` | 交易所代码 |
| `instrument_id` | `str` | 合约代码 |
| `open` | `float` | 开盘价 |
| `close` | `float` | 收盘价 |
| `low` | `float` | 最低价 |
| `high` | `float` | 最高价 |
| `volume` | `int` | 成交量 |
| `open_interest` | `int` | 持仓量 |
| `datetime` | `TypeDateTime` | 时间 |

*`exchange` 和 `instrument_id` 两个字段是在 v2025.0424 之后的版本新增的*

**成员 2 项**：[to_json](KLineData.to_json.md)、[update](KLineData.update.md)
