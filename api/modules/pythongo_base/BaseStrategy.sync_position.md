---
title: "BaseStrategy.sync_position"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#sync_position"
---


# `BaseStrategy.sync_position`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#sync_position)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#sync_position)

同步持仓数据函数

该方法会从无限易获取**所有帐号**的持仓并存储到 `self._position` 中。 使用 `self.get_position()` 函数时，会自动调用该方法，如无特殊情况，自己无需调用。
