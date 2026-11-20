---
title: "Position.get_single_position"
module: "pythongo.classdef"
kind: "function"
scope: "Position"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_classdef/position#get_single_position"
---


# `Position.get_single_position`


- 模块: `pythongo.classdef` › `Position`  ·  [类总览](Position.md)  ·  [整页](../../../../docs/modules/pythongo_classdef/position.md#get_single_position)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_classdef/position#get_single_position)

获取单边持仓函数

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `direction` | `Literal["long", "short"]` | 持仓方向（long 多头持仓, short 空头持仓） | 必填 |

返回：

| 类型 | 描述 |
| --- | --- |
| `Position_p` | 单向持仓数据类 |
