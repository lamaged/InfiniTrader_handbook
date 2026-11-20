---
title: "MarketCenter.get_kline_data_by_day"
module: "pythongo.core"
kind: "function"
scope: "MarketCenter"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_core#get_kline_data_by_day"
---


# `MarketCenter.get_kline_data_by_day`


- 模块: `pythongo.core` › `MarketCenter`  ·  [类总览](MarketCenter.md)  ·  [整页](../../../docs/modules/pythongo_core.md#get_kline_data_by_day)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_core#get_kline_data_by_day)

按天数（交易日）获取 K 线数据

> [!WARNING]
> 此 API 有调用限制，请合理使用，否则会永久封禁 IP

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `instrument_id` | `str` | 合约代码 | 必填 |
| `day_count` | `int` | 查询 N 天的数据，正值获取基准时间戳后的数据，负值为之前 | 必填 |
| `origin` | `int` | 基准时间戳（毫秒） | `None` |
| `style` | `KLineStyleType` | K 线周期，KLineStyle 枚举值，仅支持 M1, M5, M15, M30, H1 | `KLineStyle.M1` |
| `simply` | `bool` | 极简 K 线, 只返回带有 OHLC 和时间的 K 线 | `True` |

返回：

| 类型 | 描述 |
| --- | --- |
| `list[dict]` | K 线数据 |
