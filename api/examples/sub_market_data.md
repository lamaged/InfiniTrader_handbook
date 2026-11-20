---
title: "sub_market_data"
module: "examples"
kind: "recipe"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/examples#sub_market_data"
---


# `sub_market_data`


- 模块: `examples`  ·  整页: [examples](../../docs/examples.md#sub_market_data)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/examples#sub_market_data)

订阅 `ag2602` 合约行情，并输出行情信息

```python
class Demo(...):
    def on_start(self) -> None:
        super().on_start()

        self.sub_market_data(
            exchange="SHFE",
            instrument_id="ag2602"
        )

    def on_stop(self):
        super().on_stop()

        self.unsub_market_data(
            exchange="SHFE",
            instrument_id="ag2602"
        )

    def on_tick(self, tick: TickData) -> None:
        self.output(tick)
```

---

订阅多个合约行情，并输出行情信息

```python
class Demo(...):
    def __init__(self):
        ...
        self.my_instruments = {"SHFE": "ag2602", "CZCE": "AP601"}

    def on_start(self) -> None:
        super().on_start()

        for exchange, instrument_id in self.my_instruments.items():
            self.sub_market_data(
                exchange=exchange,
                instrument_id=instrument_id
            )

    def on_stop(self):
        super().on_stop()

        for exchange, instrument_id in self.my_instruments.items():
            self.unsub_market_data(
                exchange=exchange,
                instrument_id=instrument_id
            )

    def on_tick(self, tick: TickData) -> None:
        self.output(tick)
```
