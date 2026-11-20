---
title: "BaseStrategy.get_instruments_by_product"
module: "pythongo.base"
kind: "function"
scope: "BaseStrategy"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#get_instruments_by_product"
---


# `BaseStrategy.get_instruments_by_product`


- 模块: `pythongo.base` › `BaseStrategy`  ·  [类总览](BaseStrategy.md)  ·  [整页](../../../docs/modules/pythongo_base.md#get_instruments_by_product)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#get_instruments_by_product)

查询指定品种的所有合约信息或者仅合约代码函数

> [!NOTE]
> 品种代码可以在无限易的「期权 - T 型报价」窗口查询「交易所」和「品种」字段。ETF 期权品种代码是 `ETF_O`

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `product_id` | `str` | 品种代码 | 必填 |
| `raw_data` | `bool` | 是否返回原始数据（如果传入 False 则列表中只返回合约代码） | True |

返回：

| 类型 | 描述 |
| --- | --- |
| `TypeInstResult` | 所有合约信息数据对象或者仅合约代码字段 |
