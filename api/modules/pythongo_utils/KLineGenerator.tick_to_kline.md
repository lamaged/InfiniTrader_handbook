---
title: "KLineGenerator.tick_to_kline"
module: "pythongo.utils"
kind: "function"
scope: "KLineGenerator"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-generator-tick_to_kline"
---


# `KLineGenerator.tick_to_kline`


- 模块: `pythongo.utils` › `KLineGenerator`  ·  [类总览](KLineGenerator.md)  ·  [整页](../../../docs/modules/pythongo_utils.md#kline-generator-tick_to_kline)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-generator-tick_to_kline)

合成 K 线

接收 `tick` 来合成 K 线，当 K 线周期达到设置的周期，则通过 `callback` 推送过去，如果定义了 `real_time_callback` 回调，则每次 K 线有更新，都会将最新的 K 线通过 `real_time_callback` 推送过去

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `tick` | `TickData` | tick 对象 | 必填 |
| `push` | `bool` | 直接推送 K 线（请不要填写该参数） | False |
