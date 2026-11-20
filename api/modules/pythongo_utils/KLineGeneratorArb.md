---
title: "KLineGeneratorArb"
module: "pythongo.utils"
kind: "class"
import: "from pythongo.utils import KLineGeneratorArb"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-generator-arb"
---


# `KLineGeneratorArb`


- 模块: `pythongo.utils`  ·  整页: [modules/pythongo_utils](../../../docs/modules/pythongo_utils.md#kline-generator-arb)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#kline-generator-arb)
- `from pythongo.utils import KLineGeneratorArb`

标准套利合约的分钟级 K 线合成器

所有功能继承自 `KLineGenerator`，重新实现了 `tick_to_kline`，可以接受套利合约的两腿合约 `tick`，然后合成一个新的 `tick`，再传入到父类的 `tick_to_kline`

所有方法和属性以及用法都和 `KLineGenerator` 一样，入参也一样，这里不重复介绍了（可以去看自带的示例套利策略）

> [!NOTE]
> 支持套利合约的站点环境才能收到套利合约的行情
