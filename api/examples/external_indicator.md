---
title: "external_indicator"
module: "examples"
kind: "recipe"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/examples#external_indicator"
---


# `external_indicator`


- 模块: `examples`  ·  整页: [examples](../../docs/examples.md#external_indicator)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/examples#external_indicator)

使用**麦语言**，**通达信**和**同花顺**中常见的指标

先下载 [转换指标库文件](https://infinitrader-file.quantdo.com.cn/pythongo/strategy/MyTT.py)，然后把文件放在和无限易安装目录中的 `pyStrategy` 目录中

```text
InfiniTrader_Simulation
└── pyStrategy
    ├── pythongo
    └── MyTT.py
```

```python
from MyTT import MA

class Demo(...):
    def on_start(self) -> None:
        super().on_start()

        ma5 = MA(self.kline_generator.producer.close, 5) # 获取 5 日均线序列
        ma10 = MA(self.kline_generator.producer.close, 10) # 获取 10 日均线序列
```

别的函数使用方法，请打开该文件自行查看（该指标转换算法来源于开源项目：[MyTT](https://github.com/mpquant/MyTT)，无限易和 PythonGO 不对指标计算差异所导致的任何损失负责！）

持续更新中...
