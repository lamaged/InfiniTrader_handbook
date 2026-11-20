---
title: "BaseStrategy.get_instrument_data"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#get_instrument_data"
---


# `BaseStrategy.get_instrument_data`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#get_instrument_data)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#get_instrument_data)

获取合约信息函数

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `instrument_id` | `str` | 合约代码 | 必填 |

返回：

| 类型 | 描述 |
| --- | --- |
| `InstrumentData` | 合约信息数据对象 |
