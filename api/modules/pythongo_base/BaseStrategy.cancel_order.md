---
title: "BaseStrategy.cancel_order"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#cancel_order"
---


# `BaseStrategy.cancel_order`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#cancel_order)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#cancel_order)

撤单函数

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `order_id` | `int` | 报单编号 | 必填 |

返回：

| 类型 | 描述 |
| --- | --- |
| `int` | -1 表示报单编号不存在，0 表示撤单请求发送成功（不代表撤单成功） |
