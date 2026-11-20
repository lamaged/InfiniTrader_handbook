---
title: "KLineContainer.get"
module: "pythongo.utils"
kind: "function"
scope: "KLineContainer"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#get"
---


# `KLineContainer.get`


- 模块: `pythongo.utils` › `KLineContainer`  ·  [类总览](KLineContainer.md)  ·  [整页](../../../docs/modules/pythongo_utils.md#get)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#get)

根据交易所, 合约和 K 线分钟获取缓存的 K 线

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `instrument_id` | `str` | 合约代码 | 必填 |
| `style` | `KLineStyleType` | K 线周期 | 必填 |

返回：

| 类型 | 描述 |
| --- | --- |
| `list[dict]` | K 线数据 |
