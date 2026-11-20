---
title: "BaseStrategy.pause_strategy"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#pause_strategy"
---


# `BaseStrategy.pause_strategy`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#pause_strategy)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#pause_strategy)

暂停策略函数

效果和客户端点击暂停一样

> [!CAUTION]
> 请勿在 `on_start` 和 `on_stop` 中使用本方法，否则会进入死循环
