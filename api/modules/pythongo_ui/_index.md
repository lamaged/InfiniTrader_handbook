---
title: "pythongo.ui"
section: "modules/pythongo_ui"
---

# pythongo.ui

原文: https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_ui

| 名称 | 类型 | 说明 | 卡片 |
| --- | --- | --- | --- |
| `BaseStrategy` | class | 带 UI 的基础策略模版 | [打开](BaseStrategy.md) |
| `BaseStrategy.widget` | function |  | [打开](BaseStrategy.widget.md) |
| `BaseStrategy.main_indicator_data` | function | 注意：不能直接对该属性赋值，而应该自行定义该属性 | [打开](BaseStrategy.main_indicator_data.md) |
| `BaseStrategy.sub_indicator_data` | function | 注意：不能直接对该属性赋值，而应该自行定义该属性 | [打开](BaseStrategy.sub_indicator_data.md) |
| `KLWidget` | class | K 线组件 | [打开](KLWidget.md) |
| `KLWidget.recv_kline` | function | 收取 K 线、价格信号、指标数据，并将 K 线更新在线图上 | [打开](KLWidget.recv_kline.md) |
| `modules-description` | class |  | [打开](modules-description.md) |
| `modules-description.crosshair.py` | function | 该模块是十字光标模块，可以显示通过移动鼠标后到达的 K 线坐标对应的 K 线数据 | [打开](modules-description.crosshair.py.md) |
| `modules-description.drawer.py` | function | 绘画 K 线图 UI 的主模块，使用 PyQt 构建了整个线图的 UI | [打开](modules-description.drawer.py.md) |
| `modules-description.widget.py` | function | 连接策略与 drawer.py 的桥梁，其中包含了带 UI 功能的基础策略模版， | [打开](modules-description.widget.py.md) |
