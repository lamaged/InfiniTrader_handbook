---
title: "BaseStrategy.on_order_trade"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#on_order_trade"
---


# `BaseStrategy.on_order_trade`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#on_order_trade)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#on_order_trade)

收到报单成交推送回调

回调是 `on_order` 主动触发的，等同于 `on_trade`，最好使用 `on_trade`

参数：

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| `order` | `OrderData` | 报单数据对象 |
