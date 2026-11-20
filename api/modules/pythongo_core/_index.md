---
title: "pythongo.core"
section: "modules/pythongo_core"
---

# pythongo.core

原文: https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_core

| 名称 | 类型 | 说明 | 卡片 |
| --- | --- | --- | --- |
| `MarketCenter` | class | 数据中心 API 类 | [打开](MarketCenter.md) |
| `MarketCenter.get_kline_data` | function | 获取 K 线数据 | [打开](MarketCenter.get_kline_data.md) |
| `MarketCenter.get_kline_data_by_day` | function | 按天数（交易日）获取 K 线数据 | [打开](MarketCenter.get_kline_data_by_day.md) |
| `MarketCenter.get_dominant_list` | function | 获取交易所的主连合约列表 | [打开](MarketCenter.get_dominant_list.md) |
| `MarketCenter.get_instrument_trade_time` | function | 查询带交易日的合约交易时段 | [打开](MarketCenter.get_instrument_trade_time.md) |
| `MarketCenter.get_product_trade_time` | function | 查询品种的交易时段信息 | [打开](MarketCenter.get_product_trade_time.md) |
| `MarketCenter.get_avl_close_time` | function | 从缓存中获取合约可使用的收盘时间序列，如无缓存, 则获取不到任何数据 | [打开](MarketCenter.get_avl_close_time.md) |
| `MarketCenter.get_next_gen_time` | function | 根据提供的合约信息、时间和 K 线周期，获取下一根 K 线生成时间 | [打开](MarketCenter.get_next_gen_time.md) |
| `KLineStyle` | class | K 线周期 | [打开](KLineStyle.md) |
| `KLineStyleType` | class | K 线周期类型 | [打开](KLineStyleType.md) |
