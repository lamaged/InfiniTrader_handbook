---
title: "OptionChain"
module: "pythongo.option"
kind: "function"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_option#optionchain"
---


# `OptionChain`


- 模块: `pythongo.option`  ·  整页: [modules/pythongo_option](../../../docs/modules/pythongo_option.md#optionchain)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_option#optionchain)

该类将同一品种下的所有期权合约整合成了期权链，提供了获取标的月份合约、到期日、行权价、看涨期权、看跌期权和平值期权的方法

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `product_id` | `str` | 品种代码 | 必填 |

> [!NOTE]
> 期权的品种代码可以在无限易的「期权 - T 型报价」窗口查询「交易所」和「品种」字段。ETF 期权品种代码是 `ETF_O`

**成员 8 项**：[option_chain](OptionChain.option_chain.md)、[option_type](OptionChain.option_type.md)、[get_month_contracts](OptionChain.get_month_contracts.md)、[get_expire_dates](OptionChain.get_expire_dates.md)、[get_strike_prices](OptionChain.get_strike_prices.md)、[get_call_options](OptionChain.get_call_options.md)、[get_put_options](OptionChain.get_put_options.md)、[get_atm_option](OptionChain.get_atm_option.md)
