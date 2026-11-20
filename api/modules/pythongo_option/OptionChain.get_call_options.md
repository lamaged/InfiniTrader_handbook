---
title: "OptionChain.get_call_options"
module: "pythongo.option"
kind: "function"
scope: "OptionChain"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_option#get_call_options"
---


# `OptionChain.get_call_options`


- 模块: `pythongo.option` › `OptionChain`  ·  [类总览](OptionChain.md)  ·  [整页](../../../docs/modules/pythongo_option.md#get_call_options)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_option#get_call_options)

获取看涨期权合约列表，按行权价升序排列

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `underlying_symbol` | `str` | 标的合约代码 | 必填 |
| `expire_date` | `str` | 到期日, 仅对 ETF 期权有效，默认取最近到期日 | None |

返回：

| 类型 | 描述 |
| --- | --- |
| `list[str]` | 看涨期权合约代码列表 |
