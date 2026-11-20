# API 总览（177 张速查卡）

> 用法：先在本表按名字/说明定位，再打开对应卡片（每张只有几百字，比整页省 token）。

## examples

| 符号 | 类型 | 签名 | 说明 | 卡片 |
| --- | --- | --- | --- | --- |
| `external_indicator` | recipe | `—` | 使用麦语言，通达信和同花顺中常见的指标 | [卡片](../api/examples/external_indicator.md) |
| `get_k_kline_data` | recipe | `—` | 利用 pythongo.core 获取最近的 10 根 1 分钟 K 线 | [卡片](../api/examples/get_k_kline_data.md) |
| `get_position` | recipe | `—` | 查询 ag2602 的持仓 | [卡片](../api/examples/get_position.md) |
| `kline_generator` | recipe | `—` | 需要合成 K 线，但是不需要历史数据 | [卡片](../api/examples/kline_generator.md) |
| `kline_ui` | recipe | `—` | 自定义副图显示指标 | [卡片](../api/examples/kline_ui.md) |
| `scheduler` | recipe | `—` | 参考 深入框架 - pythongo.utils - Scheduler | [卡片](../api/examples/scheduler.md) |
| `sub_market_data` | recipe | `—` | 订阅 ag2602 合约行情，并输出行情信息 | [卡片](../api/examples/sub_market_data.md) |

## pythongo.base

| 符号 | 类型 | 签名 | 说明 | 卡片 |
| --- | --- | --- | --- | --- |
| `BaseParams` | class | `class BaseParams` | 参数映射模型 | [卡片](../api/modules/pythongo_base/BaseParams.md) |
| `BaseState` | class | `class BaseState` | 状态映射模型 | [卡片](../api/modules/pythongo_base/BaseState.md) |
| `BaseStrategy` | class | `class BaseStrategy` | 策略模板 | [卡片](../api/modules/pythongo_base/BaseStrategy.md) |
| `BaseStrategy.auto_close_position` | function | `BaseStrategy.auto_close_position(exchange, instrument_id, volume, price=报单价格, order_direction, order_type="GFD", investor="", hedgeflag="1", shfe_close_first=False, market=False, memo=None)` | 自动平仓函数（平今优先） | [卡片](../api/modules/pythongo_base/BaseStrategy.auto_close_position.md) |
| `BaseStrategy.cancel_order` | function | `BaseStrategy.cancel_order(order_id)` | 撤单函数 | [卡片](../api/modules/pythongo_base/BaseStrategy.cancel_order.md) |
| `BaseStrategy.get_account_fund_data` | function | `BaseStrategy.get_account_fund_data(investor)` | 获取账号资金数据函数 | [卡片](../api/modules/pythongo_base/BaseStrategy.get_account_fund_data.md) |
| `BaseStrategy.get_all_position` | function | `BaseStrategy.get_all_position(simple=False)` | 获取所有帐号的所有持仓 | [卡片](../api/modules/pythongo_base/BaseStrategy.get_all_position.md) |
| `BaseStrategy.get_instrument_data` | function | `BaseStrategy.get_instrument_data(exchange, instrument_id)` | 获取合约信息函数 | [卡片](../api/modules/pythongo_base/BaseStrategy.get_instrument_data.md) |
| `BaseStrategy.get_instruments_by_product` | function | `BaseStrategy.get_instruments_by_product(exchange, product_id, raw_data=True)` | 查询指定品种的所有合约信息或者仅合约代码函数 | [卡片](../api/modules/pythongo_base/BaseStrategy.get_instruments_by_product.md) |
| `BaseStrategy.get_investor_data` | function | `BaseStrategy.get_investor_data(index=1)` | 获取投资者信息函数 | [卡片](../api/modules/pythongo_base/BaseStrategy.get_investor_data.md) |
| `BaseStrategy.get_params` | function | `BaseStrategy.get_params()` | 获取策略参数 | [卡片](../api/modules/pythongo_base/BaseStrategy.get_params.md) |
| `BaseStrategy.get_position` | function | `BaseStrategy.get_position(instrument_id, hedgeflag="1", investor=None, simple=False)` | 获取持仓数据函数 | [卡片](../api/modules/pythongo_base/BaseStrategy.get_position.md) |
| `BaseStrategy.load_instance_file` | function | `BaseStrategy.load_instance_file()` | 加载实例文件并对策略设置对应属性 | [卡片](../api/modules/pythongo_base/BaseStrategy.load_instance_file.md) |
| `BaseStrategy.make_order_req` | function | `BaseStrategy.make_order_req(exchange, instrument_id, volume, price=报单价格, order_direction, offset, order_type, investor, hedgeflag, market=False, memo=None)` | 发送报单请求函数 | [卡片](../api/modules/pythongo_base/BaseStrategy.make_order_req.md) |
| `BaseStrategy.on_cancel` | function | `BaseStrategy.on_cancel(order)` | 收到撤单推送回调 | [卡片](../api/modules/pythongo_base/BaseStrategy.on_cancel.md) |
| `BaseStrategy.on_contract_status` | function | `BaseStrategy.on_contract_status(status)` | 合约状态变化回调 | [卡片](../api/modules/pythongo_base/BaseStrategy.on_contract_status.md) |
| `BaseStrategy.on_error` | function | `BaseStrategy.on_error(error)` | 收到报单错误推送回调 | [卡片](../api/modules/pythongo_base/BaseStrategy.on_error.md) |
| `BaseStrategy.on_init` | function | `BaseStrategy.on_init()` | 创建实例回调 | [卡片](../api/modules/pythongo_base/BaseStrategy.on_init.md) |
| `BaseStrategy.on_order` | function | `BaseStrategy.on_order(order)` | 报单变化回调 | [卡片](../api/modules/pythongo_base/BaseStrategy.on_order.md) |
| `BaseStrategy.on_order_trade` | function | `BaseStrategy.on_order_trade(order)` | 收到报单成交推送回调 | [卡片](../api/modules/pythongo_base/BaseStrategy.on_order_trade.md) |
| `BaseStrategy.on_start` | function | `BaseStrategy.on_start()` | 启动策略回调 | [卡片](../api/modules/pythongo_base/BaseStrategy.on_start.md) |
| `BaseStrategy.on_stop` | function | `BaseStrategy.on_stop()` | 停止策略回调 | [卡片](../api/modules/pythongo_base/BaseStrategy.on_stop.md) |
| `BaseStrategy.on_tick` | function | `BaseStrategy.on_tick(tick)` | 收到行情 tick 推送回调 | [卡片](../api/modules/pythongo_base/BaseStrategy.on_tick.md) |
| `BaseStrategy.on_trade` | function | `BaseStrategy.on_trade(trade, log)` | 报单成交推送回调 | [卡片](../api/modules/pythongo_base/BaseStrategy.on_trade.md) |
| `BaseStrategy.output` | function | `BaseStrategy.output(*msg)` | 输出信息到控制台 | [卡片](../api/modules/pythongo_base/BaseStrategy.output.md) |
| `BaseStrategy.pause_strategy` | function | `BaseStrategy.pause_strategy()` | 暂停策略函数 | [卡片](../api/modules/pythongo_base/BaseStrategy.pause_strategy.md) |
| `BaseStrategy.save_instance_file` | function | `BaseStrategy.save_instance_file()` | 保存实例信息 | [卡片](../api/modules/pythongo_base/BaseStrategy.save_instance_file.md) |
| `BaseStrategy.send_order` | function | `BaseStrategy.send_order(exchange, instrument_id, volume, price=报单价格, order_direction, order_type="GFD", investor="", hedgeflag="1", market=False, memo=None)` | 报单函数（开仓） | [卡片](../api/modules/pythongo_base/BaseStrategy.send_order.md) |
| `BaseStrategy.set_params` | function | `BaseStrategy.set_params(data)` | 设置策略参数 | [卡片](../api/modules/pythongo_base/BaseStrategy.set_params.md) |
| `BaseStrategy.sub_market_data` | function | `BaseStrategy.sub_market_data(exchange=None, instrument_id=None)` | 订阅合约行情函数 | [卡片](../api/modules/pythongo_base/BaseStrategy.sub_market_data.md) |
| `BaseStrategy.sync_position` | function | `BaseStrategy.sync_position()` | 同步持仓数据函数 | [卡片](../api/modules/pythongo_base/BaseStrategy.sync_position.md) |
| `BaseStrategy.unsub_market_data` | function | `BaseStrategy.unsub_market_data(exchange=None, instrument_id=None)` | 取消订阅合约行情函数 | [卡片](../api/modules/pythongo_base/BaseStrategy.unsub_market_data.md) |
| `BaseStrategy.update_status_bar` | function | `BaseStrategy.update_status_bar()` | 更新无限易 PythonGO 窗口状态栏显示值 | [卡片](../api/modules/pythongo_base/BaseStrategy.update_status_bar.md) |
| `BaseStrategy.class_name` | attribute | `属性` | 类型：str | [卡片](../api/modules/pythongo_base/BaseStrategy.class_name.md) |
| `BaseStrategy.exchange_list` | attribute | `属性` | 类型：list[str] | [卡片](../api/modules/pythongo_base/BaseStrategy.exchange_list.md) |
| `BaseStrategy.instance_file` | attribute | `属性` | 类型：str | [卡片](../api/modules/pythongo_base/BaseStrategy.instance_file.md) |
| `BaseStrategy.instrument_list` | attribute | `属性` | 类型：list[str] | [卡片](../api/modules/pythongo_base/BaseStrategy.instrument_list.md) |
| `BaseStrategy.limit_time` | attribute | `属性` | 类型：int | [卡片](../api/modules/pythongo_base/BaseStrategy.limit_time.md) |
| `BaseStrategy.params_map` | attribute | `属性` | 类型：BaseParams | [卡片](../api/modules/pythongo_base/BaseStrategy.params_map.md) |
| `BaseStrategy.state_map` | attribute | `属性` | 类型：BaseState | [卡片](../api/modules/pythongo_base/BaseStrategy.state_map.md) |
| `BaseStrategy.strategy_id` | attribute | `属性` | 类型：int | [卡片](../api/modules/pythongo_base/BaseStrategy.strategy_id.md) |
| `BaseStrategy.strategy_name` | attribute | `属性` | 类型：str | [卡片](../api/modules/pythongo_base/BaseStrategy.strategy_name.md) |
| `BaseStrategy.trading` | attribute | `属性` | 类型：bool | [卡片](../api/modules/pythongo_base/BaseStrategy.trading.md) |
| `inherit` | section | `—` | 在 Python 中，子类通过继承语法继承父类后，可以拥有父类的所有属性或方法，这样极大的减少了重复的代码，可以让代码更加简洁高效。 | [卡片](../api/modules/pythongo_base/inherit.md) |

## pythongo.classdef

| 符号 | 类型 | 签名 | 说明 | 卡片 |
| --- | --- | --- | --- | --- |
| `AccountData` | class | `class AccountData` | 账户数据类 | [卡片](../api/modules/pythongo_classdef/account/AccountData.md) |
| `CancelOrderData` | class | `class CancelOrderData` | 撤单数据类 | [卡片](../api/modules/pythongo_classdef/order/CancelOrderData.md) |
| `InstrumentData` | class | `class InstrumentData` | 合约数据类 | [卡片](../api/modules/pythongo_classdef/instrument/InstrumentData.md) |
| `InstrumentStatus` | class | `class InstrumentStatus` | 合约状态类 | [卡片](../api/modules/pythongo_classdef/instrument/InstrumentStatus.md) |
| `InvestorData` | class | `class InvestorData` | 投资者数据类 | [卡片](../api/modules/pythongo_classdef/investor/InvestorData.md) |
| `KLineData` | class | `class KLineData` | K 线数据类 | [卡片](../api/modules/pythongo_classdef/kline/KLineData.md) |
| `ObjDataType` | class | `class ObjDataType` | dict[str, str \| int \| float] | [卡片](../api/modules/pythongo_classdef/common/ObjDataType.md) |
| `OrderData` | class | `class OrderData` | 报单数据类 | [卡片](../api/modules/pythongo_classdef/order/OrderData.md) |
| `Position` | class | `class Position` | 合约持仓数据类 | [卡片](../api/modules/pythongo_classdef/position/Position.md) |
| `Position_p` | class | `class Position_p` | 单向持仓数据类 | [卡片](../api/modules/pythongo_classdef/position/Position_p.md) |
| `TickData` | class | `class TickData` | 行情切片数据类 | [卡片](../api/modules/pythongo_classdef/tick/TickData.md) |
| `TradeData` | class | `class TradeData` | 成交数据类 | [卡片](../api/modules/pythongo_classdef/trade/TradeData.md) |
| `KLineData.to_json` | function | `KLineData.to_json()` | K 线对象转字典 | [卡片](../api/modules/pythongo_classdef/kline/KLineData.to_json.md) |
| `KLineData.update` | function | `KLineData.update(**kwargs)` | 更新 K 线属性 | [卡片](../api/modules/pythongo_classdef/kline/KLineData.update.md) |
| `Position.get_single_position` | function | `Position.get_single_position(direction)` | 获取单边持仓函数 | [卡片](../api/modules/pythongo_classdef/position/Position.get_single_position.md) |
| `TickData.copy` | function | `TickData.copy()` | 浅拷贝自身 | [卡片](../api/modules/pythongo_classdef/tick/TickData.copy.md) |
| `TickData.update` | function | `TickData.update(**kwargs)` | 更新属性（正常情况下使用不到） | [卡片](../api/modules/pythongo_classdef/tick/TickData.update.md) |

## pythongo.core

| 符号 | 类型 | 签名 | 说明 | 卡片 |
| --- | --- | --- | --- | --- |
| `KLineStyle` | class | `class KLineStyle` | K 线周期 | [卡片](../api/modules/pythongo_core/KLineStyle.md) |
| `KLineStyleType` | class | `class KLineStyleType` | K 线周期类型 | [卡片](../api/modules/pythongo_core/KLineStyleType.md) |
| `MarketCenter` | class | `class MarketCenter` | 数据中心 API 类 | [卡片](../api/modules/pythongo_core/MarketCenter.md) |
| `MarketCenter.get_avl_close_time` | function | `MarketCenter.get_avl_close_time(instrument_id)` | 从缓存中获取合约可使用的收盘时间序列，如无缓存, 则获取不到任何数据 | [卡片](../api/modules/pythongo_core/MarketCenter.get_avl_close_time.md) |
| `MarketCenter.get_dominant_list` | function | `MarketCenter.get_dominant_list(exchange)` | 获取交易所的主连合约列表 | [卡片](../api/modules/pythongo_core/MarketCenter.get_dominant_list.md) |
| `MarketCenter.get_instrument_trade_time` | function | `MarketCenter.get_instrument_trade_time(exchange, instrument_id, instant=None)` | 查询带交易日的合约交易时段 | [卡片](../api/modules/pythongo_core/MarketCenter.get_instrument_trade_time.md) |
| `MarketCenter.get_kline_data` | function | `MarketCenter.get_kline_data(exchange, instrument_id, style=KLineStyle.M1, count=-1440, origin=None, start_time=None, end_time=None, simply=True)` | 获取 K 线数据 | [卡片](../api/modules/pythongo_core/MarketCenter.get_kline_data.md) |
| `MarketCenter.get_kline_data_by_day` | function | `MarketCenter.get_kline_data_by_day(exchange, instrument_id, day_count, origin=None, style=KLineStyle.M1, simply=True)` | 按天数（交易日）获取 K 线数据 | [卡片](../api/modules/pythongo_core/MarketCenter.get_kline_data_by_day.md) |
| `MarketCenter.get_next_gen_time` | function | `MarketCenter.get_next_gen_time(exchange, instrument_id, tick_time, style)` | 根据提供的合约信息、时间和 K 线周期，获取下一根 K 线生成时间 | [卡片](../api/modules/pythongo_core/MarketCenter.get_next_gen_time.md) |
| `MarketCenter.get_product_trade_time` | function | `MarketCenter.get_product_trade_time(exchange, product_id, trading_day=None)` | 查询品种的交易时段信息 | [卡片](../api/modules/pythongo_core/MarketCenter.get_product_trade_time.md) |

## pythongo.indicator

| 符号 | 类型 | 签名 | 说明 | 卡片 |
| --- | --- | --- | --- | --- |
| `Indicators` | class | `class Indicators` | 技术指标类 | [卡片](../api/modules/pythongo_indicator/Indicators.md) |
| `Indicators.adx` | function | `Indicators.adx()` | 平均趋向指数（Average Directional Index） | [卡片](../api/modules/pythongo_indicator/Indicators.adx.md) |
| `Indicators.atr` | function | `Indicators.atr()` | 真实波幅均值（Average True Range） | [卡片](../api/modules/pythongo_indicator/Indicators.atr.md) |
| `Indicators.bbi` | function | `Indicators.bbi()` | 多空指数（Bull And Bear lndex） | [卡片](../api/modules/pythongo_indicator/Indicators.bbi.md) |
| `Indicators.boll` | function | `Indicators.boll()` | 布林线指标（Bollinger Bands） | [卡片](../api/modules/pythongo_indicator/Indicators.boll.md) |
| `Indicators.cci` | function | `Indicators.cci()` | 顺势指标（Commodity Channel Index） | [卡片](../api/modules/pythongo_indicator/Indicators.cci.md) |
| `Indicators.donchian` | function | `Indicators.donchian()` | 唐奇安通道（Donchian Channels） | [卡片](../api/modules/pythongo_indicator/Indicators.donchian.md) |
| `Indicators.ema` | function | `Indicators.ema()` | 指数平均数（EXPMA(Exponential Moving Average)） | [卡片](../api/modules/pythongo_indicator/Indicators.ema.md) |
| `Indicators.kd` | function | `Indicators.kd()` | 随机指标 | [卡片](../api/modules/pythongo_indicator/Indicators.kd.md) |
| `Indicators.kdj` | function | `Indicators.kdj()` | 随机指标 | [卡片](../api/modules/pythongo_indicator/Indicators.kdj.md) |
| `Indicators.keltner` | function | `Indicators.keltner()` | 肯特纳通道指标（Keltner Channels） | [卡片](../api/modules/pythongo_indicator/Indicators.keltner.md) |
| `Indicators.macd` | function | `Indicators.macd()` | 指数平滑移动平均线（Moving Average Convergence and Divergence） | [卡片](../api/modules/pythongo_indicator/Indicators.macd.md) |
| `Indicators.macdext` | function | `Indicators.macdext()` | MACD 扩展方法，具有可控 MA 类型的 MACD，可对每个周期设置不同的 MA 类型 | [卡片](../api/modules/pythongo_indicator/Indicators.macdext.md) |
| `Indicators.rsi` | function | `Indicators.rsi()` | 相对强弱指数（Relative Strength Index） | [卡片](../api/modules/pythongo_indicator/Indicators.rsi.md) |
| `Indicators.sar` | function | `Indicators.sar()` | 抛物线指标（Parabolic Stop and Reverse） | [卡片](../api/modules/pythongo_indicator/Indicators.sar.md) |
| `Indicators.sma` | function | `Indicators.sma()` | 简单移动平均线（Simple Moving Average） | [卡片](../api/modules/pythongo_indicator/Indicators.sma.md) |
| `Indicators.std` | function | `Indicators.std()` | 标准差（StdDev(Standard Deviation)） | [卡片](../api/modules/pythongo_indicator/Indicators.std.md) |

## pythongo.infini

| 符号 | 类型 | 签名 | 说明 | 卡片 |
| --- | --- | --- | --- | --- |
| `cancel_order` | function | `cancel_order()` | 撤单函数 | [卡片](../api/modules/pythongo_infini/cancel_order.md) |
| `get_instrument` | function | `get_instrument()` | 获取合约信息 | [卡片](../api/modules/pythongo_infini/get_instrument.md) |
| `get_instruments_by_product` | function | `get_instruments_by_product()` | 查询指定品种的所有合约信息 | [卡片](../api/modules/pythongo_infini/get_instruments_by_product.md) |
| `get_investor_account` | function | `get_investor_account()` | 获取账号资金数据 | [卡片](../api/modules/pythongo_infini/get_investor_account.md) |
| `get_investor_list` | function | `get_investor_list()` | 获取所有的投资者信息 | [卡片](../api/modules/pythongo_infini/get_investor_list.md) |
| `get_investor_position` | function | `get_investor_position()` | 获取账号持仓 | [卡片](../api/modules/pythongo_infini/get_investor_position.md) |
| `pause_strategy` | function | `pause_strategy()` | 暂停策略 | [卡片](../api/modules/pythongo_infini/pause_strategy.md) |
| `send_order` | function | `send_order()` | 发单函数 | [卡片](../api/modules/pythongo_infini/send_order.md) |
| `sub_market_data` | function | `sub_market_data()` | 订阅合约行情 | [卡片](../api/modules/pythongo_infini/sub_market_data.md) |
| `unsub_market_data` | function | `unsub_market_data()` | 取消订阅合约行情 | [卡片](../api/modules/pythongo_infini/unsub_market_data.md) |
| `update_param` | function | `update_param()` | 界面传入参数在实例中更新 | [卡片](../api/modules/pythongo_infini/update_param.md) |
| `update_state` | function | `update_state()` | 更新无限易 PythonGO 窗口状态栏显示值 | [卡片](../api/modules/pythongo_infini/update_state.md) |
| `write_log` | function | `write_log()` | 输出日志到控制台 | [卡片](../api/modules/pythongo_infini/write_log.md) |

## pythongo.option

| 符号 | 类型 | 签名 | 说明 | 卡片 |
| --- | --- | --- | --- | --- |
| `Option` | class | `class Option` | 该类提供期权扩展功能，可以计算期权希腊值，由于代码陈旧冗长，这里不过多介绍，具体实现可以自行查阅代码。 | [卡片](../api/modules/pythongo_option/Option.md) |
| `OptionChain` | function | `OptionChain()` | 该类将同一品种下的所有期权合约整合成了期权链，提供了获取标的月份合约、到期日、行权价、看涨期权、看跌期权和平值期权的方法 | [卡片](../api/modules/pythongo_option/OptionChain.md) |
| `OptionChain.get_atm_option` | function | `OptionChain.get_atm_option(underlying_symbol, underlying_price, expire_date=None)` | 获取平值期权档位 | [卡片](../api/modules/pythongo_option/OptionChain.get_atm_option.md) |
| `OptionChain.get_call_options` | function | `OptionChain.get_call_options(underlying_symbol, expire_date=None)` | 获取看涨期权合约列表，按行权价升序排列 | [卡片](../api/modules/pythongo_option/OptionChain.get_call_options.md) |
| `OptionChain.get_expire_dates` | function | `OptionChain.get_expire_dates(underlying_symbol=None)` | 获取标的月份合约的到期日列表，按到期时间排序 | [卡片](../api/modules/pythongo_option/OptionChain.get_expire_dates.md) |
| `OptionChain.get_month_contracts` | function | `OptionChain.get_month_contracts()` | 获取标的月份合约列表，按到期时间排序 | [卡片](../api/modules/pythongo_option/OptionChain.get_month_contracts.md) |
| `OptionChain.get_put_options` | function | `OptionChain.get_put_options(underlying_symbol, expire_date=None)` | 获取看跌期权合约列表，按行权价升序排列 | [卡片](../api/modules/pythongo_option/OptionChain.get_put_options.md) |
| `OptionChain.get_strike_prices` | function | `OptionChain.get_strike_prices(underlying_symbol, expire_date=None)` | 获取行权价列表，升序排列 | [卡片](../api/modules/pythongo_option/OptionChain.get_strike_prices.md) |
| `OptionChain.option_chain` | attribute | `属性` | 类型：dict | [卡片](../api/modules/pythongo_option/OptionChain.option_chain.md) |
| `OptionChain.option_type` | attribute | `属性` | 类型：Literal["期权", "股票期权", "现货期权"] | [卡片](../api/modules/pythongo_option/OptionChain.option_type.md) |

## pythongo.types

| 符号 | 类型 | 签名 | 说明 | 卡片 |
| --- | --- | --- | --- | --- |
| `TypeDateTime` | class | `class TypeDateTime` | 时间类型，等同于 datetime.datetime | [卡片](../api/modules/pythongo_types/TypeDateTime.md) |
| `TypeHedgeFlag` | class | `class TypeHedgeFlag` | 投机套保标志 | [卡片](../api/modules/pythongo_types/TypeHedgeFlag.md) |
| `TypeInstResult` | class | `class TypeInstResult` | 合约信息数据类型 | [卡片](../api/modules/pythongo_types/TypeInstResult.md) |
| `TypeOffsetFlag` | class | `class TypeOffsetFlag` | 开平标志 | [卡片](../api/modules/pythongo_types/TypeOffsetFlag.md) |
| `TypeOrderDIR` | class | `class TypeOrderDIR` | 报单方向 | [卡片](../api/modules/pythongo_types/TypeOrderDIR.md) |
| `TypeOrderFlag` | class | `class TypeOrderFlag` | 报单指令 | [卡片](../api/modules/pythongo_types/TypeOrderFlag.md) |
| `TypeProduct` | class | `class TypeProduct` | 品种类型 | [卡片](../api/modules/pythongo_types/TypeProduct.md) |
| `TypeRAWOrderFlag` | class | `class TypeRAWOrderFlag` | 原始报单指令 | [卡片](../api/modules/pythongo_types/TypeRAWOrderFlag.md) |

## pythongo.ui

| 符号 | 类型 | 签名 | 说明 | 卡片 |
| --- | --- | --- | --- | --- |
| `BaseStrategy` | class | `class BaseStrategy` | 带 UI 的基础策略模版 | [卡片](../api/modules/pythongo_ui/BaseStrategy.md) |
| `KLWidget` | class | `class KLWidget` | K 线组件 | [卡片](../api/modules/pythongo_ui/KLWidget.md) |
| `modules-description` | class | `class modules-description` |  | [卡片](../api/modules/pythongo_ui/modules-description.md) |
| `BaseStrategy.main_indicator_data` | function | `BaseStrategy.main_indicator_data()` | 注意：不能直接对该属性赋值，而应该自行定义该属性 | [卡片](../api/modules/pythongo_ui/BaseStrategy.main_indicator_data.md) |
| `BaseStrategy.sub_indicator_data` | function | `BaseStrategy.sub_indicator_data()` | 注意：不能直接对该属性赋值，而应该自行定义该属性 | [卡片](../api/modules/pythongo_ui/BaseStrategy.sub_indicator_data.md) |
| `BaseStrategy.widget` | function | `BaseStrategy.widget()` |  | [卡片](../api/modules/pythongo_ui/BaseStrategy.widget.md) |
| `KLWidget.recv_kline` | function | `KLWidget.recv_kline(data=数据容器)` | 收取 K 线、价格信号、指标数据，并将 K 线更新在线图上 | [卡片](../api/modules/pythongo_ui/KLWidget.recv_kline.md) |
| `modules-description.crosshair.py` | function | `modules-description.crosshair.py()` | 该模块是十字光标模块，可以显示通过移动鼠标后到达的 K 线坐标对应的 K 线数据 | [卡片](../api/modules/pythongo_ui/modules-description.crosshair.py.md) |
| `modules-description.drawer.py` | function | `modules-description.drawer.py()` | 绘画 K 线图 UI 的主模块，使用 PyQt 构建了整个线图的 UI | [卡片](../api/modules/pythongo_ui/modules-description.drawer.py.md) |
| `modules-description.widget.py` | function | `modules-description.widget.py()` | 连接策略与 drawer.py 的桥梁，其中包含了带 UI 功能的基础策略模版，还有 KLWidget 简化库，可以将 K 线数据传递给 U | [卡片](../api/modules/pythongo_ui/modules-description.widget.py.md) |

## pythongo.utils

| 符号 | 类型 | 签名 | 说明 | 卡片 |
| --- | --- | --- | --- | --- |
| `CustomLogHandler` | class | `class CustomLogHandler` | 自定义日志 Handler | [卡片](../api/modules/pythongo_utils/CustomLogHandler.md) |
| `KLineGeneratorArb` | class | `class KLineGeneratorArb` | 标准套利合约的分钟级 K 线合成器 | [卡片](../api/modules/pythongo_utils/KLineGeneratorArb.md) |
| `KLineContainer` | function | `KLineContainer()` | K 线容器 | [卡片](../api/modules/pythongo_utils/KLineContainer.md) |
| `KLineGenerator` | function | `KLineGenerator()` | 分钟级 K 线合成 | [卡片](../api/modules/pythongo_utils/KLineGenerator.md) |
| `KLineGeneratorSec` | function | `KLineGeneratorSec()` | 秒级 K 线生成器 | [卡片](../api/modules/pythongo_utils/KLineGeneratorSec.md) |
| `KLineProducer` | function | `KLineProducer()` | K 线生产器 | [卡片](../api/modules/pythongo_utils/KLineProducer.md) |
| `Scheduler` | function | `Scheduler()` | 简易定时器 | [卡片](../api/modules/pythongo_utils/Scheduler.md) |
| `isdigit` | function | `isdigit()` | 判断字符串是否整数或小数 | [卡片](../api/modules/pythongo_utils/isdigit.md) |
| `split_arbitrage_code` | function | `split_arbitrage_code()` | 分割套利合约代码 | [卡片](../api/modules/pythongo_utils/split_arbitrage_code.md) |
| `KLineContainer.get` | function | `KLineContainer.get(exchange, instrument_id, style)` | 根据交易所, 合约和 K 线分钟获取缓存的 K 线 | [卡片](../api/modules/pythongo_utils/KLineContainer.get.md) |
| `KLineContainer.init` | function | `KLineContainer.init(exchange, instrument_id, style)` | 获取合约 K 线并缓存 | [卡片](../api/modules/pythongo_utils/KLineContainer.init.md) |
| `KLineContainer.set` | function | `KLineContainer.set(exchange, instrument_id, style, data)` | 根据交易所, 合约和 K 线分钟缓存 K 线 | [卡片](../api/modules/pythongo_utils/KLineContainer.set.md) |
| `KLineGenerator.push_history_data` | function | `KLineGenerator.push_history_data()` | 推送历史 K 线数据到回调 | [卡片](../api/modules/pythongo_utils/KLineGenerator.push_history_data.md) |
| `KLineGenerator.stop_push_scheduler` | function | `KLineGenerator.stop_push_scheduler()` | 停止推送每个交易时段最后一根 K 线的定时器 | [卡片](../api/modules/pythongo_utils/KLineGenerator.stop_push_scheduler.md) |
| `KLineGenerator.tick_to_kline` | function | `KLineGenerator.tick_to_kline(tick, push=False)` | 合成 K 线 | [卡片](../api/modules/pythongo_utils/KLineGenerator.tick_to_kline.md) |
| `KLineGeneratorSec.tick_to_kline` | function | `KLineGeneratorSec.tick_to_kline(tick)` | 合成秒级 K 线 | [卡片](../api/modules/pythongo_utils/KLineGeneratorSec.tick_to_kline.md) |
| `KLineProducer.append_data` | function | `KLineProducer.append_data(kline)` | 添加 K 线数据 | [卡片](../api/modules/pythongo_utils/KLineProducer.append_data.md) |
| `KLineProducer.insert_data` | function | `KLineProducer.insert_data(kline, index=-1)` | 根据数组下标插入 K 线数据 | [卡片](../api/modules/pythongo_utils/KLineProducer.insert_data.md) |
| `KLineProducer.update` | function | `KLineProducer.update(kline)` | 更新数据序列 | [卡片](../api/modules/pythongo_utils/KLineProducer.update.md) |
| `KLineProducer.update_last_kline` | function | `KLineProducer.update_last_kline(kline)` | 更新最后一根 K 线数据 | [卡片](../api/modules/pythongo_utils/KLineProducer.update_last_kline.md) |
| `KLineProducer.worker` | function | `KLineProducer.worker()` | 将 K 线数据转成 K 线对象后更新到本实例中的 K 线数据序列，并且推送到 K 线回调中，这部分数据也称 K 线历史数据 | [卡片](../api/modules/pythongo_utils/KLineProducer.worker.md) |
| `Scheduler.add_job` | function | `Scheduler.add_job(func, trigger, id=None)` | 添加定时任务 | [卡片](../api/modules/pythongo_utils/Scheduler.add_job.md) |
| `Scheduler.get_job` | function | `Scheduler.get_job(job_id)` | 根据 job_id 获取对应的定时任务 | [卡片](../api/modules/pythongo_utils/Scheduler.get_job.md) |
| `Scheduler.get_jobs` | function | `Scheduler.get_jobs()` | 返回所有定时任务 | [卡片](../api/modules/pythongo_utils/Scheduler.get_jobs.md) |
| `Scheduler.remove_job` | function | `Scheduler.remove_job(job_id)` | 根据 job_id 移除定时任务 | [卡片](../api/modules/pythongo_utils/Scheduler.remove_job.md) |
| `Scheduler.start` | function | `Scheduler.start()` | 启动定时器 | [卡片](../api/modules/pythongo_utils/Scheduler.start.md) |
| `Scheduler.stop` | function | `Scheduler.stop()` | 停止定时器 | [卡片](../api/modules/pythongo_utils/Scheduler.stop.md) |
| `KLineGenerator.exchange` | attribute | `属性` | 类型：str | [卡片](../api/modules/pythongo_utils/KLineGenerator.exchange.md) |
| `KLineGenerator.instrument_id` | attribute | `属性` | 类型：str | [卡片](../api/modules/pythongo_utils/KLineGenerator.instrument_id.md) |
| `KLineGenerator.producer` | attribute | `属性` | 类型：KLineProducer | [卡片](../api/modules/pythongo_utils/KLineGenerator.producer.md) |
| `KLineGenerator.style` | attribute | `属性` | 类型：KLineStyleType | [卡片](../api/modules/pythongo_utils/KLineGenerator.style.md) |
| `KLineProducer.close` | attribute | `属性` | 类型：list[np.float64] | [卡片](../api/modules/pythongo_utils/KLineProducer.close.md) |
| `KLineProducer.datetime` | attribute | `属性` | 类型：list[TypeDateTime] | [卡片](../api/modules/pythongo_utils/KLineProducer.datetime.md) |
| `KLineProducer.exchange` | attribute | `属性` | 类型：str | [卡片](../api/modules/pythongo_utils/KLineProducer.exchange.md) |
| `KLineProducer.high` | attribute | `属性` | 类型：list[np.float64] | [卡片](../api/modules/pythongo_utils/KLineProducer.high.md) |
| `KLineProducer.instrument_id` | attribute | `属性` | 类型：str | [卡片](../api/modules/pythongo_utils/KLineProducer.instrument_id.md) |
| `KLineProducer.kline_container` | attribute | `属性` | 类型：KLineContainer | [卡片](../api/modules/pythongo_utils/KLineProducer.kline_container.md) |
| `KLineProducer.low` | attribute | `属性` | 类型：list[np.float64] | [卡片](../api/modules/pythongo_utils/KLineProducer.low.md) |
| `KLineProducer.open` | attribute | `属性` | 类型：list[np.float64] | [卡片](../api/modules/pythongo_utils/KLineProducer.open.md) |
| `KLineProducer.style` | attribute | `属性` | 类型：KLineStyleType | [卡片](../api/modules/pythongo_utils/KLineProducer.style.md) |
| `KLineProducer.volume` | attribute | `属性` | 类型：list[np.float64] | [卡片](../api/modules/pythongo_utils/KLineProducer.volume.md) |

