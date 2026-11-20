---
title: "split_arbitrage_code"
module: "pythongo.utils"
kind: "function"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#split_arbitrage_code"
---


# `split_arbitrage_code`


- 模块: `pythongo.utils`  ·  整页: [modules/pythongo_utils](../../../docs/modules/pythongo_utils.md#split_arbitrage_code)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#split_arbitrage_code)

分割套利合约代码

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `instrument_id` | `str` | 标准套利合约代码 | 必填 |

返回：

| 类型 | 描述 |
| --- | --- |
| `tuple[Optional[str], Optional[str]] ` | 两腿合约 |
