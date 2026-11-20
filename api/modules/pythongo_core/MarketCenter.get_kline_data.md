---
title: "MarketCenter.get_kline_data"
module: "pythongo.core"
kind: "function"
scope: "MarketCenter"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_core#get_kline_data"
---


# `MarketCenter.get_kline_data`


- 模块: `pythongo.core` › `MarketCenter`  ·  [类总览](MarketCenter.md)  ·  [整页](../../../docs/modules/pythongo_core.md#get_kline_data)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_core#get_kline_data)

获取 K 线数据

> [!WARNING]
> 此 API 有调用限制，请合理使用，否则会永久封禁 IP

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `instrument_id` | `str` | 合约代码 | 必填 |
| `style` | `KLineStyleType` | K 线周期, KLineStyle 枚举值 | `KLineStyle.M1` |
| `count` | `int` | 查询的 K 线数量（最大 1440），正值获取基准时间戳后的数据，负值为之前 | `-1440` |
| `origin` | `int` | 基准时间戳（毫秒） | `None` |
| `start_time` | `TypeDateTime` | K 线开始时间 | `None` |
| `end_time` | `TypeDateTime` | K 线结束时间 | `None` |
| `simply` | `bool` | 极简 K 线, 只返回带有 OHLC 和时间的 K 线 | `True` |

返回：

| 类型 | 描述 |
| --- | --- |
| `list[dict]` | K 线数据 |

注意：

使用 `start_time` 和 `end_time` 可以获取一个时间区间的 K 线，但同时这样会忽略 `count` 和 `origin` 参数

也就是说要么按时间区间获取，要么按 K 线数量获取 K 线数据
