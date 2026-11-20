---
title: "TradeData"
module: "pythongo.classdef"
kind: "class"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_classdef/trade#tradedata"
---


# `TradeData`


- 模块: `pythongo.classdef`  ·  整页: [modules/pythongo_classdef/trade](../../../../docs/modules/pythongo_classdef/trade.md#tradedata)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_classdef/trade#tradedata)

成交数据类

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| `exchange` | `str` | 交易所代码 |
| `instrument_id` | `str` | 合约代码 |
| `trade_id` | `str` | 成交编号 |
| `order_id` | `int` | 报单编号 |
| `order_sys_id` | `str` | 交易所报单编号 |
| `trade_time` | `str` | 成交时间 |
| `direction` | `str` | 买卖方向 |
| `offset` | `TypeOffsetFlag` | 开平标志 |
| `hedgeflag` | `TypeHedgeFlag` | 投机套保标志 |
| `price` | `float` | 成交价格 |
| `volume` | `int` | 成交数量 |
| `memo` | `str` | 报单备注 |

买卖方向 `direction` 具体信息请查看 [数值映射 - DirectionType](../../../../docs/faq/mapping.md#directiontype)

开平标志 `offset` 具体信息请查看 [数值映射 - OffsetFlagType](../../../../docs/faq/mapping.md#offsetflagtype)

投机套保标志 `hedgeflag` 具体信息请查看 [数值映射 - HedgeFlagType](../../../../docs/faq/mapping.md#hedgeflagtype)
