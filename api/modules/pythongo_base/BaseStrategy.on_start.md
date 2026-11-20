---
title: "BaseStrategy.on_start"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#on_start"
---


# `BaseStrategy.on_start`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#on_start)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#on_start)

启动策略回调

界面点击运行按钮会触发此方法

> [!NOTE]
> 此方法会将 `self.trading` 设置为 `True`，然后订阅合约行情
