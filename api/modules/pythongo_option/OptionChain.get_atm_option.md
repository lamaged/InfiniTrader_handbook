---
title: "OptionChain.get_atm_option"
module: "pythongo.option"
kind: "function"
scope: "OptionChain"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_option#get_atm_option"
---


# `OptionChain.get_atm_option`


- 模块: `pythongo.option` › `OptionChain`  ·  [类总览](OptionChain.md)  ·  [整页](../../../docs/modules/pythongo_option.md#get_atm_option)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_option#get_atm_option)

获取平值期权档位

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `underlying_symbol` | `str` | 标的合约代码 | 必填 |
| `underlying_price` | `float` | 标的价格 | 必填 |
| `expire_date` | `str` | 到期日, 仅对 ETF 期权有效，默认取最近到期日 | None |

返回：

| 类型 | 描述 |
| --- | --- |
| `Optional[int]` | 获取最接近标的价格的行权价在行权价列表中的索引位置，可根据索引从看涨期权列表和看跌期权列表中获取平值看涨期权和平值看跌期权 |
