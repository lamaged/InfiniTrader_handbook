---
title: "kline_ui"
module: "examples"
kind: "recipe"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/examples#kline_ui"
---


# `kline_ui`


- 模块: `examples`  ·  整页: [examples](../../docs/examples.md#kline_ui)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/examples#kline_ui)

自定义副图显示指标

定义 `sub_indicator_data`，然后传参给 `self.widget.recv_kline`

```python
class Demo(...):
    @property
    def sub_indicator_data(self) -> dict[str, float]:
        """副图指标"""
        return {
            "K": ...,
            "D": ...,
            "J": ...,
        }

    def callback(self, kline: KLineData) -> None:
        """接受 K 线回调"""
        self.widget.recv_kline({
            "kline": ...,
            **self.sub_indicator_data
        })
```
