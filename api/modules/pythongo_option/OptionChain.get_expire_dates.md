---
title: "OptionChain.get_expire_dates"
module: "pythongo.option"
kind: "function"
scope: "OptionChain"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_option#get_expire_dates"
---


# `OptionChain.get_expire_dates`


- 模块: `pythongo.option` › `OptionChain`  ·  [类总览](OptionChain.md)  ·  [整页](../../../docs/modules/pythongo_option.md#get_expire_dates)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_option#get_expire_dates)

获取标的月份合约的到期日列表，按到期时间排序

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `underlying_symbol` | `str` | 标的合约代码 | None |

返回：

| 类型 | 描述 |
| --- | --- |
| `list[str]` | 标的月份合约期权到期日 |

> [!NOTE]
> 当 `underlying_symbol` 为 `None` 时，返回所有月份合约的到期日,例如 `IO` 返回：`['20250919', '20251017', '20251121', '20251219', '20260320', '20260619']`；
>
> 当 `underlying_symbol` 填入参数时，返回填入标的合约的到期日，例如 `IF2509` 返回：`['20250919']`；
>
> 当 `underlying_symbol` 填入 ETF 合约代码时，返回 ETF 合约的到期日列表，例如 `510050` 返回：`['20250924', '20251022', '20251224', '20260325']`
