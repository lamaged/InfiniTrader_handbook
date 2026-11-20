---
title: "get_k_kline_data"
module: "examples"
kind: "recipe"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/examples#get_k_kline_data"
---


# `get_k_kline_data`


- 模块: `examples`  ·  整页: [examples](../../docs/examples.md#get_k_kline_data)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/examples#get_k_kline_data)

利用 `pythongo.core` 获取最近的 10 根 1 分钟 K 线

```python
from pythongo.core import MarketCenter

class Demo(...):
    def __init__(self) -> None:
        super().__init__()
        self.market_center = MarketCenter()

    def on_start(self) -> None:
        super().on_start()

        kline_data = self.market_center.get_kline_data(
            exchange="SHFE",
            instrument_id="ag2406",
            style="M1",
            count=-10
        )
```

---

利用 `pythongo.core` 获取 `2024-01-31 14:30` 到 `2024-01-31 15:00` 的 1 分钟 K 线

```python
from datetime import datetime

from pythongo.core import MarketCenter

class Demo(...):
    def __init__(self) -> None:
        super().__init__()
        self.market_center = MarketCenter()

    def on_start(self) -> None:
        super().on_start()

        kline_data = self.market_center.get_kline_data(
            exchange="SHFE",
            instrument_id="ag2406",
            style="M1",
            start_time=datetime(2024, 1, 31, 14, 30),
            end_time=datetime(2024, 1, 31, 15)
        )
```
