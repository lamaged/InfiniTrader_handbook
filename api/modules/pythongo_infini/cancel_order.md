---
title: "cancel_order"
module: "pythongo.infini"
kind: "function"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_infini#cancel_order"
---


# `cancel_order`


- 模块: `pythongo.infini`  ·  整页: [modules/pythongo_infini](../../../docs/modules/pythongo_infini.md#cancel_order)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_infini#cancel_order)

撤单函数

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `order_id` | `int` | 报单编号 | 必填 |

返回：

| 类型 | 描述 |
| --- | --- |
| `int` | -1 表示 order_id 不存在，0 表示撤单请求发送成功（不代表撤单成功） |
