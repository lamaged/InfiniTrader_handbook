---
title: "MarketCenter.get_next_gen_time"
module: "pythongo.core"
kind: "function"
scope: "MarketCenter"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_core#get_next_gen_time"
---


# `MarketCenter.get_next_gen_time`


- 模块: `pythongo.core` › `MarketCenter`  ·  [类总览](MarketCenter.md)  ·  [整页](../../../docs/modules/pythongo_core.md#get_next_gen_time)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_core#get_next_gen_time)

根据提供的合约信息、时间和 K 线周期，获取下一根 K 线生成时间

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `instrument_id` | `str` | 合约代码 | 必填 |
| `tick_time` | `datetime` | tick 时间 | 必填 |
| `style` | `KLineStyleType` | K 线周期, KLineStyle 枚举值 | 必填 |

返回：

| 类型 | 描述 |
| --- | --- |
| `datetime` | 下一根 K 线生成时间 |
