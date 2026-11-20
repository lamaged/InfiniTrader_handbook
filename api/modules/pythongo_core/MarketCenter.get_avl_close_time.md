---
title: "MarketCenter.get_avl_close_time"
module: "pythongo.core"
kind: "function"
scope: "MarketCenter"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_core#get_avl_close_time"
---


# `MarketCenter.get_avl_close_time`


- 模块: `pythongo.core` › `MarketCenter`  ·  [类总览](MarketCenter.md)  ·  [整页](../../../docs/modules/pythongo_core.md#get_avl_close_time)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_core#get_avl_close_time)

从缓存中获取合约可使用的收盘时间序列，如无缓存, 则获取不到任何数据

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `instrument_id` | `str` | 合约代码 | 必填 |

返回：

| 类型 | 描述 |
| --- | --- |
| `list[datetime]` | 在当前时间之后的收盘时间序列 |
