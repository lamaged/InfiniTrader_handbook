---
title: "BaseStrategy.instrument_list"
module: "pythongo.base"
kind: "attribute"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#instrument_list"
---


# `BaseStrategy.instrument_list`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#instrument_list)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#instrument_list)

类型：`list[str]`

合约列表

通过分号分割 `params_map` 中的 `instrument_id` 得到

实现方法为：

```python
self.params_map.instrument_id.split(";")
```
