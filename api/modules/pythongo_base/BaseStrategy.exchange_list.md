---
title: "BaseStrategy.exchange_list"
module: "pythongo.base"
kind: "attribute"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#exchange_list"
---


# `BaseStrategy.exchange_list`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#exchange_list)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#exchange_list)

类型：`list[str]`

交易所列表

通过分号分割 `params_map` 中的 `exchange` 得到

实现方法为：

```python
self.params_map.exchange.split(";")
```
