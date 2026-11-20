---
title: "KLWidget.recv_kline"
module: "pythongo.ui"
kind: "function"
scope: "KLWidget"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_ui#recv_kline"
---


# `KLWidget.recv_kline`


- 模块: `pythongo.ui` › `KLWidget`  ·  [类总览](KLWidget.md)  ·  [整页](../../../docs/modules/pythongo_ui.md#recv_kline)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_ui#recv_kline)

收取 K 线、价格信号、指标数据，并将 K 线更新在线图上

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `data` | `dict[str, float \| KLineData]` | 数据容器 | 必填 |

data 包含 K 线数据、价格信号、指标数据

举例：`{"kline": kline_data, "signal_price": 0.0, "MA": 0.0}`
