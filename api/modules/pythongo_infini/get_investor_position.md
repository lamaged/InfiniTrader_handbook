---
title: "get_investor_position"
module: "pythongo.infini"
kind: "function"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_infini#get_investor_position"
---


# `get_investor_position`


- 模块: `pythongo.infini`  ·  整页: [modules/pythongo_infini](../../../docs/modules/pythongo_infini.md#get_investor_position)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_infini#get_investor_position)

获取账号持仓

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `investor` | `str` | 投资者账号 | 必填 |
| `Simple` | `bool` | 简化持仓数据（但持仓是实时的） | False |

> [!NOTE]
> `Simple` 字段在 `v2025.0522` 后的版本中新增，当 `Simple` 为 `True` 的时候，获取到的持仓是实时的，不会再有延迟的情况，但是持仓数据中不会有以下这些字段：`PositionCost`, `YdPositionCost`, `CloseProfit`, `PositionProfit`, `OpenAvgPrice`, `PositionAvgPrice`, `UsedMargin`

返回：

| 类型 | 描述 |
| --- | --- |
| `list[ObjDataType]` | 账号持仓数据 |
