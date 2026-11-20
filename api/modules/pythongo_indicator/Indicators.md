---
title: "Indicators"
module: "pythongo.indicator"
kind: "class"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_indicator#indicators"
---


# `Indicators`


- 模块: `pythongo.indicator`  ·  整页: [modules/pythongo_indicator](../../../docs/modules/pythongo_indicator.md#indicators)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_indicator#indicators)

技术指标类

依赖于 [`KLineProducer`](../../../docs/modules/pythongo_utils.md#kline-producer)，`KLineProducer` 继承本类后，拥有本类的指标计算方法，且提供 `OHLC` 数据，你应该注意到，本类中是没有定义 `OHLC` 的，一切属性都来自于 `KLineProducer`，所以依赖于 `KLineProducer`。

本类中所有指标都已经设置好默认值（周期），所以可以直接调用而无需填写参数，如需自己填写参数，可以根据编辑器提示，或者查阅本类的代码来传入对应的参数，这里就不对参数做过多的解释了。

**成员 16 项**：[sma](Indicators.sma.md)、[ema](Indicators.ema.md)、[std](Indicators.std.md)、[bbi](Indicators.bbi.md)、[cci](Indicators.cci.md)、[rsi](Indicators.rsi.md)、[adx](Indicators.adx.md)、[sar](Indicators.sar.md)、[kdj](Indicators.kdj.md)、[kd](Indicators.kd.md)、[macd](Indicators.macd.md)、[macdext](Indicators.macdext.md)、[atr](Indicators.atr.md)、[boll](Indicators.boll.md)、[keltner](Indicators.keltner.md)、[donchian](Indicators.donchian.md)
