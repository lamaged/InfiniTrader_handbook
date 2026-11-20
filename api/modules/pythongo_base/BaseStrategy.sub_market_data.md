---
title: "BaseStrategy.sub_market_data"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#sub_market_data"
---


# `BaseStrategy.sub_market_data`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#sub_market_data)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#sub_market_data)

订阅合约行情函数

> [!NOTE]
> 使用此方法订阅合约时，交易所代码和合约代码可以为空，当两者为空时，会自动取 `self.exchange_list` 和 `self.instrument_list` 中的合约来订阅

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | None |
| `instrument_id` | `str` | 合约代码 | None |
