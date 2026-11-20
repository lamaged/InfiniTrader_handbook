---
title: "pythongo.indicator"
url: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_indicator"
---

# pythongo.indicator

本模块为技术指标实现，基于 talib 封装

<a id="indicators"></a>
## Indicators

技术指标类

依赖于 [`KLineProducer`](pythongo_utils.md#kline-producer)，`KLineProducer` 继承本类后，拥有本类的指标计算方法，且提供 `OHLC` 数据，你应该注意到，本类中是没有定义 `OHLC` 的，一切属性都来自于 `KLineProducer`，所以依赖于 `KLineProducer`。

本类中所有指标都已经设置好默认值（周期），所以可以直接调用而无需填写参数，如需自己填写参数，可以根据编辑器提示，或者查阅本类的代码来传入对应的参数，这里就不对参数做过多的解释了。

<a id="sma"></a>
### `sma()`

简单移动平均线（Simple Moving Average）

<a id="ema"></a>
### `ema()`

指数平均数（EXPMA(Exponential Moving Average)）

<a id="std"></a>
### `std()`

标准差（StdDev(Standard Deviation)）

<a id="bbi"></a>
### `bbi()`

多空指数（Bull And Bear lndex）

<a id="cci"></a>
### `cci()`

顺势指标（Commodity Channel Index）

<a id="rsi"></a>
### `rsi()`

相对强弱指数（Relative Strength Index）

<a id="adx"></a>
### `adx()`

平均趋向指数（Average Directional Index）

<a id="sar"></a>
### `sar()`

抛物线指标（Parabolic Stop and Reverse）

<a id="kdj"></a>
### `kdj()`

随机指标

<a id="kd"></a>
### `kd()`

随机指标

<a id="macd"></a>
### `macd()`

指数平滑移动平均线（Moving Average Convergence and Divergence）

<a id="macdext"></a>
### `macdext()`

MACD 扩展方法，具有可控 MA 类型的 MACD，可对每个周期设置不同的 MA 类型

支持以下 MA 类型（*matype）：

- 0: SMA (simple)
- 1: EMA (exponential)
- 2: WMA (weighted)
- 3: DEMA (double exponential)
- 4: TEMA (triple exponential)
- 5: TRIMA (triangular)
- 6: KAMA (Kaufman adaptive)
- 7: MAMA (Mesa adaptive)
- 8: T3 (triple exponential T3)

具体使用方法请自行查看函数实现

<a id="atr"></a>
### `atr()`

真实波幅均值（Average True Range）

<a id="boll"></a>
### `boll()`

布林线指标（Bollinger Bands）

<a id="keltner"></a>
### `keltner()`

肯特纳通道指标（Keltner Channels）

<a id="donchian"></a>
### `donchian()`

唐奇安通道（Donchian Channels）
