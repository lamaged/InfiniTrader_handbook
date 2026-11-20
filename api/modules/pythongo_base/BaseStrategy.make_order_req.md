---
title: "BaseStrategy.make_order_req"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#make_order_req"
---


# `BaseStrategy.make_order_req`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#make_order_req)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#make_order_req)

发送报单请求函数

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `instrument_id` | `str` | 合约代码 | 必填 |
| `volume` | `int` | 报单手数 | 必填 |
| `price` | `float \| int` | 报单价格 | 必填 |
| `order_direction` | `TypeOrderDIR` | 报单方向（大写） | 必填 |
| `offset` | `TypeOffsetFlag` | 开平标志 | 必填 |
| `order_type` | `TypeOrderFlag` | 报单指令 | 必填 |
| `investor` | `str` | 报单账号 | 必填 |
| `hedgeflag` | `TypeHedgeFlag` | 投机套保标志 | 必填 |
| `market` | `bool` | True 市价单，False 非市价单 | False |
| `memo` | `Any` | 报单备注 | None |

返回：

| 类型 | 描述 |
| --- | --- |
| `int` | 报单编号（-1 为报单失败） |
