---
title: "KLineGeneratorSec"
module: "pythongo.utils"
kind: "function"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-generator-sec"
---


# `KLineGeneratorSec`


- 模块: `pythongo.utils`  ·  整页: [modules/pythongo_utils](../../../docs/modules/pythongo_utils.md#kline-generator-sec)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-generator-sec)

秒级 K 线生成器

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `callback` | `Callable[[KLineData], None]` | 推送 K 线回调 | 必填 |
| `seconds` | `int` | 合成秒数 | 1 |

**成员 1 项**：[tick_to_kline](KLineGeneratorSec.tick_to_kline.md)
