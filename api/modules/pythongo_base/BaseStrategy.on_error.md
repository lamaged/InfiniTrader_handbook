---
title: "BaseStrategy.on_error"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#on_error"
---


# `BaseStrategy.on_error`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#on_error)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#on_error)

收到报单错误推送回调

参数：

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| `error` | `dict[str, str]` | 错误信息 包含 errCode (错误代码), errMsg (错误信息), orderID (报单编号) |

其中有几点需要注意：

- 当 `errCode` 为 `0004` 的时候，是撤单错误，你可以根据该值做一些撤单错误后的处理。
- 函数运行错误和报单错误都会进入此回调，所以 `error` 如果有 `orderID` 键，那就是属于报单错误的回调，反之则是函数运行错误
