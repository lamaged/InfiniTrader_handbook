---
title: "MarketCenter.get_product_trade_time"
module: "pythongo.core"
kind: "function"
scope: "MarketCenter"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_core#get_product_trade_time"
---


# `MarketCenter.get_product_trade_time`


- 模块: `pythongo.core` › `MarketCenter`  ·  [类总览](MarketCenter.md)  ·  [整页](../../../docs/modules/pythongo_core.md#get_product_trade_time)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_core#get_product_trade_time)

查询品种的交易时段信息

> [!WARNING]
> 此 API 有调用限制，请合理使用，否则会永久封禁 IP

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `product_id` | `str` | 品种代码，也可填写合约代码 | 必填 |
| `trading_day` | `str` | 品种交易日，格式为 `%Y%m%d`，例如：20240101 | `None` |

返回：

| 类型 | 描述 |
| --- | --- |
| `dict` | 品种交易时段信息 |
