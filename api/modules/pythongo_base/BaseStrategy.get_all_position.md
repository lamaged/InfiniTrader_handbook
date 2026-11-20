---
title: "BaseStrategy.get_all_position"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#get_all_position"
---


# `BaseStrategy.get_all_position`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#get_all_position)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#get_all_position)

获取所有帐号的所有持仓

> [!NOTE]
> 本函数在 `v2025.1112` 版本新增

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `simple` | `bool` | 简化持仓数据（但持仓是实时的） | False |

返回：

| 类型 | 描述 |
| --- | --- |
| `dict[str, dict[str, dict[str, Position]]]` | 所有帐号的所有持仓 |

> [!NOTE]
> 返回的数据类型为字典，如要取合约双向持仓，顺序为：投资者帐号 -> 合约代码 -> 投机套保标志，参考代码：`position.get(investor, {}).get(instrument_id, {}).get(hedgeflag)`
