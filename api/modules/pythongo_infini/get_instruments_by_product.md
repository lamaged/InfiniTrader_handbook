---
title: "get_instruments_by_product"
module: "pythongo.infini"
kind: "function"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_infini#get_instruments_by_product"
---


# `get_instruments_by_product`


- 模块: `pythongo.infini`  ·  整页: [modules/pythongo_infini](../../../docs/modules/pythongo_infini.md#get_instruments_by_product)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_infini#get_instruments_by_product)

查询指定品种的所有合约信息

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `exchange` | `str` | 交易所代码 | 必填 |
| `product_id` | `str` | 品种代码 | 必填 |

返回：

| 类型 | 描述 |
| --- | --- |
| `list[ObjDataType]` | 指定品种的所有合约信息 |
