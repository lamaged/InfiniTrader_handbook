---
title: "OptionChain.get_month_contracts"
module: "pythongo.option"
kind: "function"
scope: "OptionChain"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_option#get_month_contracts"
---


# `OptionChain.get_month_contracts`


- 模块: `pythongo.option` › `OptionChain`  ·  [类总览](OptionChain.md)  ·  [整页](../../../docs/modules/pythongo_option.md#get_month_contracts)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_option#get_month_contracts)

获取标的月份合约列表，按到期时间排序

返回：

| 类型 | 描述 |
| --- | --- |
| `list[str]` | 月份合约列表 |

> [!NOTE]
> ETF 期权没有月份合约，只返回 ETF 合约列表，例如：`['510050', '510300', '510500', '588000', '588080']`
