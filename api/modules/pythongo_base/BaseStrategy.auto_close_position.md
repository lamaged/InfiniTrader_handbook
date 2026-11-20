---
title: "BaseStrategy.auto_close_position"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#auto_close_position"
---


# `BaseStrategy.auto_close_position`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#auto_close_position)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#auto_close_position)

自动平仓函数（平今优先）

> [!WARNING]
> 当平上期所、能源中心仓位的时候，如果既平了昨仓，又平了今仓，只会返回最后一次平仓的报单编号

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `instrument_id` | `str` | 合约代码 | 必填 |
| `volume` | `int` | 报单手数 | 必填 |
| `price` | `float \| int` | 报单价格 | 必填 |
| `order_direction` | `TypeOrderDIR` | 报单方向 | 必填 |
| `order_type` | `TypeOrderFlag` | 报单指令 | "GFD" |
| `investor` | `str` | 报单账号 | "" |
| `hedgeflag` | `TypeHedgeFlag` | 投机套保标志 | "1" |
| `shfe_close_first` | `bool` | 上期平仓（昨仓）优先 | False |
| `market` | `bool` | True 市价单，False 非市价单 | False |
| `memo` | `Any` | 报单备注 | None |

返回：

| 类型 | 描述 |
| --- | --- |
| `int \| None` | 报单编号（-1 为报单失败） |
