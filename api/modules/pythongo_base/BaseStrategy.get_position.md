---
title: "BaseStrategy.get_position"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#get_position"
---


# `BaseStrategy.get_position`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#get_position)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#get_position)

获取持仓数据函数

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `instrument_id` | `str` | 合约代码 | 必填 |
| `hedgeflag` | `TypeHedgeFlag` | 投机套保标志 | "1" |
| `investor` | `str` | 资金账号（默认使用查询到的第一个帐号） | None |
| `simple` | `bool` | 简化持仓数据（但持仓是实时的） | False |

> [!NOTE]
> `simple` 字段在 `v2025.0522` 后的版本中新增，当 `simple` 为 `True` 的时候，获取到的持仓是实时的，不会再有延迟的情况，但是以下这些字段没有数据：`position_cost`, `yd_position_cost`, `close_profit`, `position_profit`, `open_avg_price`, `position_avg_price`, `used_margin`，具体字段的中文说明请看：[深入框架 - pythongo.classdef - position](../../../docs/modules/pythongo_classdef/position.md#position_p)

返回：

| 类型 | 描述 |
| --- | --- |
| `Position` | 单合约的双向持仓数据 |
