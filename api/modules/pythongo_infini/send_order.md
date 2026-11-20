---
title: "send_order"
module: "pythongo.infini"
kind: "function"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_infini#send_order"
---


# `send_order`


- 模块: `pythongo.infini`  ·  整页: [modules/pythongo_infini](../../../docs/modules/pythongo_infini.md#send_order)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_infini#send_order)

发单函数

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `strategy_id` | `int` | 策略实例 ID | 必填 |
| `exchange` | `str` | 交易所代码 | 必填 |
| `instrument_id` | `str` | 合约代码 | 必填 |
| `volume` | `int` | 报单数量 | 必填 |
| `price` | `int \| float` | 报单价格 | 必填 |
| `direction` | `Literal["0", "1"]` | 报单方向：`0` 买，`1` 卖 | 必填 |
| `order_type` | `TypeRAWOrderFlag` | 报单类型：`0` GFD, `1` FAK, `2` FOK | 必填 |
| `investor` | `str` | 投资者账号 | 必填 |
| `hedgeflag` | `TypeHedgeFlag` | 投机套保标志：1 投机, 2 套利, 3 套保, 4 做市商, 5 备兑 | 必填 |
| `offset` | `TypeOffsetFlag` | 开平标志 | 必填 |
| `market` | `bool` | 是否市价单 | False |
| `memo` | `Any` | 报单备注 | None |

返回：

| 类型 | 描述 |
| --- | --- |
| `int` | 报单编号（-1 为报单失败） |
