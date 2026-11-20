---
title: "KLineGenerator.stop_push_scheduler"
module: "pythongo.utils"
kind: "function"
scope: "KLineGenerator"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-generator-stop_push_scheduler"
---


# `KLineGenerator.stop_push_scheduler`


- 模块: `pythongo.utils` › `KLineGenerator`  ·  [类总览](KLineGenerator.md)  ·  [整页](../../../docs/modules/pythongo_utils.md#kline-generator-stop_push_scheduler)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-generator-stop_push_scheduler)

停止推送每个交易时段最后一根 K 线的定时器

> [!NOTE]
> 在当前方法中，`self.scheduler` 是单例模式，所以只会移除所有的定时任务，不会停止本类中的定时器（一般用不到本方法）
