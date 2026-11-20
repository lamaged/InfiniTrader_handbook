---
title: "KLineContainer.set"
module: "pythongo.utils"
kind: "function"
scope: "KLineContainer"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#set"
---


# `KLineContainer.set`


- 模块: `pythongo.utils` › `KLineContainer`  ·  [类总览](KLineContainer.md)  ·  [整页](../../../docs/modules/pythongo_utils.md#set)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#set)

根据交易所, 合约和 K 线分钟缓存 K 线

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `instrument_id` | `str` | 合约代码 | 必填 |
| `style` | `KLineStyleType` | K 线周期 | 必填 |
| `data` | `list[dict]` | K 线数据 | 必填 |
