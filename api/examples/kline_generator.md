---
title: "kline_generator"
module: "examples"
kind: "recipe"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/examples#kline_generator"
---


# `kline_generator`


- 模块: `examples`  ·  整页: [examples](../../docs/examples.md#kline_generator)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/examples#kline_generator)

需要合成 K 线，但是不需要历史数据

```python
class Demo(...):
    def on_start(self) -> None:
        self.kline_generator = KLineGenerator(
            real_time_callback=...,
            callback=...,
            exchange=...,
            instrument_id=...,
            style=...
        )
        super().on_start()
```

---

不需要合成 K 线，只需要 `KLineProducer`，然后计算历史数据指标

```python
class Demo(...):
    def on_start(self) -> None:
        self.kline_producer = KLineProducer(
            exchange=...,
            instrument_id=...,
            style=...,
            callback=...,
        )
        self.kline_producer.worker()

        ma10 = self.kline_producer.sma(10)
        k, d, j = self.kline_producer.kdj()

        super().on_start()
```

---

合成标准套利合约 K 线

用法和 `KLineGenerator` 一致，只是需要手动订阅单腿合约

```python
from pythongo.utils import KLineGeneratorArb

class Demo(...):
    def on_tick(self, tick: TickData) -> None:
        """收到行情 tick 推送"""
        super().on_tick(tick)

        self.kline_generator.tick_to_kline(tick)

    def on_start(self) -> None:
        self.kline_generator = KLineGeneratorArb(
            callback=...,
            exchange="CZCE",
            instrument_id="IPS AP405&SA405",
            style=...,
            real_time_callback=...
        )
        self.kline_generator.push_history_data()

        super().on_start()

        for instrument_id in self.kline_generator.instruments:
            """订阅单腿合约"""
            self.sub_market_data(
                exchange="CZCE",
                instrument_id=instrument_id
            )

    def on_stop(self) -> None:
        super().on_stop()

        for instrument_id in self.kline_generator.instruments:
            """取消订阅单腿合约"""
            self.unsub_market_data(
                exchange="CZCE",
                instrument_id=instrument_id
            )
```

---

从 K 线合成器中的 `KLineProducer` 中获取 K 线数据

```python
class Demo(...):
    def on_start(self) -> None:
        super().on_start()

        last_close_price = self.kline_generator.producer.close[-1]

        last_open_price = self.kline_generator.producer.open[-10:]
```

---

多合约同周期

注意填写交易所和合约代码时候需要按照以下格式（必须按顺序依次对应，且使用英文分号 `;` 分隔）：

交易所：`SHFE;SHFE;CZCE`

合约代码：`ag2406;ag2405;AP405`

注意计算指标的时候使用正确的 `kline_generator`

```python
from pythongo.classdef import TickData
from pythongo.utils import KLineGenerator

class Demo(...):
    def __init__(self) -> None:
        self.kline_generators: dict[str, KLineGenerator] = {}
        """K 线合成器容器"""

    def on_start(self) -> None:
        for exchange, instrument_id in zip(self.exchange_list, self.instrument_list):
            kline_generator = KLineGenerator(
                real_time_callback=self.real_time_callback,
                callback=self.callback,
                exchange=exchange,
                instrument_id=instrument_id,
                style=self.params_map.kline_style
            )

            kline_generator.push_history_data()

            self.kline_generators[instrument_id] = kline_generator

        super().on_start()

    def on_tick(self, tick: TickData) -> None:
        """收到行情 tick 推送"""
        super().on_tick(tick)
        if tick.instrument_id not in self.kline_generators:
            return

        self.kline_generators[tick.instrument_id].tick_to_kline(tick)

    def calc_indicator(self) -> None:
        """计算指标数据"""

        self.kline_generators["ag2406"].producer.sma()

        self.kline_generators[self.instrument_list[0]].producer.sma()
```

---

多合约不同周期

注意填写交易所、合约代码、K 线周期时候需要按照以下格式（必须按顺序依次对应，且使用英文分号 `;` 分隔）：

交易所：`SHFE;SHFE;CZCE`

合约代码：`ag2406;ag2405;AP405`

K 线周期：`M1;M5;M10`

```python
from pythongo.classdef import TickData
from pythongo.core import KLineStyleType
from pythongo.utils import KLineGenerator

class Demo(...):
    def __init__(self) -> None:
        self.kline_generators: dict[str, dict[KLineStyleType, KLineGenerator]] = {}
        """K 线合成器容器"""

    @property
    def style_list(self) -> list[KLineStyleType]:
        """手动拆分 K 线周期"""
        return self.params_map.kline_style.split(";")

    def on_start(self) -> None:
        for exchange, instrument_id, style in zip(self.exchange_list, self.instrument_list, self.style_list):
            kline_generator = KLineGenerator(
                real_time_callback=self.real_time_callback,
                callback=self.callback,
                exchange=exchange,
                instrument_id=instrument_id,
                style=style
            )

            kline_generator.push_history_data()

            self.kline_generators[instrument_id] = {style: kline_generator}

        super().on_start()

    def on_tick(self, tick: TickData) -> None:
        """收到行情 tick 推送"""
        super().on_tick(tick)
        if tick.instrument_id not in self.kline_generators:
            return

        style_container = self.kline_generators[tick.instrument_id]

        for kline_generator in style_container.values():
            kline_generator.tick_to_kline(tick)

    def calc_indicator(self) -> None:
        """计算指标数据"""

        self.kline_generators["ag2406"]["M1"].producer.sma()

        instrument_id = self.instrument_list[0]
        style = self.style_list[0]

        self.kline_generators[instrument_id][style].producer.sma()
```
