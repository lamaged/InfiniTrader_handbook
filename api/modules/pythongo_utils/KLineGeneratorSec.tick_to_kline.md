---
title: "KLineGeneratorSec.tick_to_kline"
module: "pythongo.utils"
kind: "function"
scope: "KLineGeneratorSec"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-generator-sec-tick_to_kline"
---


# `KLineGeneratorSec.tick_to_kline`


- 模块: `pythongo.utils` › `KLineGeneratorSec`  ·  [类总览](KLineGeneratorSec.md)  ·  [整页](../../../docs/modules/pythongo_utils.md#kline-generator-sec-tick_to_kline)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-generator-sec-tick_to_kline)

合成秒级 K 线

接收 `tick` 来合成 K 线，当 K 线周期达到设置的周期，则通过上面传入的 `callback` 推送过去

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `tick` | `TickData` | tick 对象 | 必填 |
