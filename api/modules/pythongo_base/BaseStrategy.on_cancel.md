---
title: "BaseStrategy.on_cancel"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#on_cancel"
---


# `BaseStrategy.on_cancel`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#on_cancel)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#on_cancel)

收到撤单推送回调

> [!NOTE]
> 本函数在 `v2025.0801` 版本新增，新版本请使用本回调，旧版本的 `on_order_cancel` 将在未来被弃用

参数：

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| `order` | `CancelOrderData` | 撤单数据对象 |
