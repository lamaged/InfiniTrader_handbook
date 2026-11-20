---
title: "OrderData"
module: "pythongo.classdef"
kind: "class"
import: "from pythongo.classdef import OrderData"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_classdef/order#orderdata"
---


# `OrderData`


- 模块: `pythongo.classdef`  ·  整页: [modules/pythongo_classdef/order](../../../../docs/modules/pythongo_classdef/order.md#orderdata)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_classdef/order#orderdata)
- `from pythongo.classdef import OrderData`

报单数据类

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| `exchange` | `str` | 交易所代码 |
| `instrument_id` | `str` | 合约代码 |
| `order_id` | `int` | 报单编号 |
| `order_sys_id` | `str` | 交易所报单编号 |
| `price` | `float` | 报单价格 |
| `order_price_type` | `str` | 报单类型 |
| `total_volume` | `int` | 报单数量 |
| `traded_volume` | `int` | 已经成交数量 |
| `cancel_volume` | `int` | 撤单数量 |
| `direction` | `str` | 买卖方向 |
| `offset` | `TypeOffsetFlag` | 开平标志 |
| `hedgeflag` | `TypeHedgeFlag` | 投机套保标志 |
| `status` | `OrderStatusType` | 报单状态 |
| `memo` | `str` | 报单备注 |
| `front_id` | `int` | 前置编号 |
| `session_id` | `int` | 会话编号 |
| `cancel_time` | `str` | 撤单时间 |
| `order_time` | `str` | 报单时间 |

报单类型 `order_price_type` 具体信息请查看 [数值映射 - OrderPriceType](../../../../docs/faq/mapping.md#orderpricetype)

买卖方向 `direction` 具体信息请查看 [数值映射 - DirectionType](../../../../docs/faq/mapping.md#directiontype)

开平标志 `offset` 具体信息请查看 [数值映射 - OffsetFlagType](../../../../docs/faq/mapping.md#offsetflagtype)

报单状态 `status` 具体信息请查看 [数值映射 - OrderStatus](../../../../docs/faq/mapping.md#orderstatus)
