---
title: "KLineGenerator"
module: "pythongo.utils"
kind: "function"
import: "from pythongo.utils import KLineGenerator"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-generator"
---


# `KLineGenerator`


- 模块: `pythongo.utils`  ·  整页: [modules/pythongo_utils](../../../docs/modules/pythongo_utils.md#kline-generator)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-generator)
- `from pythongo.utils import KLineGenerator`

分钟级 K 线合成

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `instrument_id` | `str` | 合约代码 | 必填 |
| `callback` | `Callable[[KLineData], None]` | 推送 K 线回调 | 必填 |
| `style` | `KLineStyleType` | 合成 K 线周期 | `KLineStyle.M1` |
| `real_time_callback` | `Callable[[KLineData], None]` | 实时推送 K 线回调, 推送频率和 tick 相同 | `None` |

**成员 7 项**：[exchange](KLineGenerator.exchange.md)、[instrument_id](KLineGenerator.instrument_id.md)、[style](KLineGenerator.style.md)、[producer](KLineGenerator.producer.md)、[push_history_data](KLineGenerator.push_history_data.md)、[stop_push_scheduler](KLineGenerator.stop_push_scheduler.md)、[tick_to_kline](KLineGenerator.tick_to_kline.md)
