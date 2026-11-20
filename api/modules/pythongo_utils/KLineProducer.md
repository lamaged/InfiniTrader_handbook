---
title: "KLineProducer"
module: "pythongo.utils"
kind: "function"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-producer"
---


# `KLineProducer`


- 模块: `pythongo.utils`  ·  整页: [modules/pythongo_utils](../../../docs/modules/pythongo_utils.md#kline-producer)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-producer)

K 线生产器

本类继承了 `Indicators`（[技术指标类](../../../docs/modules/pythongo_indicator.md)），所以可以直接使用对应的指标方法

本类可以单独使用，前提是你完全了解本类的用法，且不需要最新的 K 线数据，因为本类的数据一旦获取，不会再更新，除非手动更新

实例化本类会自动实例化 `KLineContainer`

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `instrument_id` | `str` | 合约代码 | 必填 |
| `style` | `KLineStyleType` | K 线周期 | "M1" |
| `callback` | `Callable[[KLineData], None]` | 推送 K 线回调 | None |

**成员 15 项**：[exchange](KLineProducer.exchange.md)、[instrument_id](KLineProducer.instrument_id.md)、[style](KLineProducer.style.md)、[kline_container](KLineProducer.kline_container.md)、[open](KLineProducer.open.md)、[close](KLineProducer.close.md)、[high](KLineProducer.high.md)、[low](KLineProducer.low.md)、[volume](KLineProducer.volume.md)、[datetime](KLineProducer.datetime.md)、[update](KLineProducer.update.md)、[append_data](KLineProducer.append_data.md)、[insert_data](KLineProducer.insert_data.md)、[update_last_kline](KLineProducer.update_last_kline.md)、[worker](KLineProducer.worker.md)
