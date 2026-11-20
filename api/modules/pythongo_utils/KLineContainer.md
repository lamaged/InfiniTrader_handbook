---
title: "KLineContainer"
module: "pythongo.utils"
kind: "function"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-container"
---


# `KLineContainer`


- 模块: `pythongo.utils`  ·  整页: [modules/pythongo_utils](../../../docs/modules/pythongo_utils.md#kline-container)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-container)

K 线容器

可以自动缓存实例本身, 重复的交易所及合约不再重新获取 K 线

本类很简单，获取 K 线数据后，把数据缓存起来，然后供取用，但是数据不会自己更新（需要配合 `KLineGenerator` 合成 K 线后自动更新数据），所以一般不单独使用，如果只是需要取 K 线的话，可以查阅 [深入框架 - pythongo.core](../../../docs/modules/pythongo_core.md)

实例化本类后会自动调用 `init()` 方法来获取 K 线并缓存

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `instrument_id` | `str` | 合约代码 | 必填 |
| `style` | `KLineStyleType` | K 线周期 | 必填 |

**成员 3 项**：[get](KLineContainer.get.md)、[set](KLineContainer.set.md)、[init](KLineContainer.init.md)
