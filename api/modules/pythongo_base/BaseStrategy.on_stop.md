---
title: "BaseStrategy.on_stop"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#on_stop"
---


# `BaseStrategy.on_stop`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#on_stop)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#on_stop)

停止策略回调

界面点击暂停按钮会触发此方法

> [!NOTE]
> 此方法会将 `self.trading` 设置为 `False`，保存实例信息，然后取消订阅合约行情
