# 速查表（一行一个 API，只有签名）

> 需要参数含义/返回类型时再打开 `index/api.md` 或对应卡片。

## pythongo.base

```python
class BaseParams
class BaseState
class BaseStrategy
BaseStrategy.get_params()
BaseStrategy.set_params(data)
BaseStrategy.update_status_bar()
BaseStrategy.save_instance_file()
BaseStrategy.load_instance_file()
BaseStrategy.on_init()
BaseStrategy.on_start()
BaseStrategy.on_stop()
BaseStrategy.on_tick(tick)
BaseStrategy.on_contract_status(status)
BaseStrategy.on_cancel(order)
BaseStrategy.on_order_trade(order)
BaseStrategy.on_order(order)
BaseStrategy.on_trade(trade, log)
BaseStrategy.on_error(error)
BaseStrategy.pause_strategy()
BaseStrategy.output(*msg)
BaseStrategy.sub_market_data(exchange=None, instrument_id=None)
BaseStrategy.unsub_market_data(exchange=None, instrument_id=None)
BaseStrategy.sync_position()
BaseStrategy.get_all_position(simple=False)
BaseStrategy.get_position(instrument_id, hedgeflag="1", investor=None, simple=False)
BaseStrategy.send_order(exchange, instrument_id, volume, price=报单价格, order_direction, order_type="GFD", investor="", hedgeflag="1", market=False, memo=None)
BaseStrategy.auto_close_position(exchange, instrument_id, volume, price=报单价格, order_direction, order_type="GFD", investor="", hedgeflag="1", shfe_close_first=False, market=False, memo=None)
BaseStrategy.cancel_order(order_id)
BaseStrategy.make_order_req(exchange, instrument_id, volume, price=报单价格, order_direction, offset, order_type, investor, hedgeflag, market=False, memo=None)
BaseStrategy.get_account_fund_data(investor)
BaseStrategy.get_instrument_data(exchange, instrument_id)
BaseStrategy.get_instruments_by_product(exchange, product_id, raw_data=True)
BaseStrategy.get_investor_data(index=1)
BaseStrategy.strategy_id  # 属性
BaseStrategy.strategy_name  # 属性
BaseStrategy.params_map  # 属性
BaseStrategy.state_map  # 属性
BaseStrategy.limit_time  # 属性
BaseStrategy.trading  # 属性
BaseStrategy.class_name  # 属性
BaseStrategy.exchange_list  # 属性
BaseStrategy.instrument_list  # 属性
BaseStrategy.instance_file  # 属性
```

## pythongo.classdef

```python
class AccountData
class ObjDataType
class InstrumentData
class InstrumentStatus
class InvestorData
class KLineData
class OrderData
class CancelOrderData
class Position
class Position_p
class TickData
class TradeData
KLineData.to_json()
KLineData.update(**kwargs)
Position.get_single_position(direction)
TickData.copy()
TickData.update(**kwargs)
```

## pythongo.core

```python
class MarketCenter
class KLineStyle
class KLineStyleType
MarketCenter.get_kline_data(exchange, instrument_id, style=KLineStyle.M1, count=-1440, origin=None, start_time=None, end_time=None, simply=True)
MarketCenter.get_kline_data_by_day(exchange, instrument_id, day_count, origin=None, style=KLineStyle.M1, simply=True)
MarketCenter.get_dominant_list(exchange)
MarketCenter.get_instrument_trade_time(exchange, instrument_id, instant=None)
MarketCenter.get_product_trade_time(exchange, product_id, trading_day=None)
MarketCenter.get_avl_close_time(instrument_id)
MarketCenter.get_next_gen_time(exchange, instrument_id, tick_time, style)
```

## pythongo.indicator

```python
class Indicators
Indicators.sma()
Indicators.ema()
Indicators.std()
Indicators.bbi()
Indicators.cci()
Indicators.rsi()
Indicators.adx()
Indicators.sar()
Indicators.kdj()
Indicators.kd()
Indicators.macd()
Indicators.macdext()
Indicators.atr()
Indicators.boll()
Indicators.keltner()
Indicators.donchian()
```

## pythongo.infini

```python
update_param()
update_state()
pause_strategy()
write_log()
sub_market_data()
unsub_market_data()
send_order()
cancel_order()
get_instrument()
get_instruments_by_product()
get_investor_list()
get_investor_account()
get_investor_position()
```

## pythongo.option

```python
class Option
OptionChain()
OptionChain.get_month_contracts()
OptionChain.get_expire_dates(underlying_symbol=None)
OptionChain.get_strike_prices(underlying_symbol, expire_date=None)
OptionChain.get_call_options(underlying_symbol, expire_date=None)
OptionChain.get_put_options(underlying_symbol, expire_date=None)
OptionChain.get_atm_option(underlying_symbol, underlying_price, expire_date=None)
OptionChain.option_chain  # 属性
OptionChain.option_type  # 属性
```

## pythongo.types

```python
class TypeDateTime
class TypeProduct
class TypeInstResult
class TypeOrderDIR
class TypeHedgeFlag
class TypeOrderFlag
class TypeRAWOrderFlag
class TypeOffsetFlag
```

## pythongo.ui

```python
class BaseStrategy
class KLWidget
class modules-description
BaseStrategy.widget()
BaseStrategy.main_indicator_data()
BaseStrategy.sub_indicator_data()
KLWidget.recv_kline(data=数据容器)
modules-description.crosshair.py()
modules-description.drawer.py()
modules-description.widget.py()
```

## pythongo.utils

```python
class CustomLogHandler
class KLineGeneratorArb
Scheduler()
Scheduler.add_job(func, trigger, id=None)
Scheduler.get_job(job_id)
Scheduler.get_jobs()
Scheduler.remove_job(job_id)
Scheduler.start()
Scheduler.stop()
KLineGeneratorSec()
KLineGeneratorSec.tick_to_kline(tick)
KLineGenerator()
KLineGenerator.push_history_data()
KLineGenerator.stop_push_scheduler()
KLineGenerator.tick_to_kline(tick, push=False)
KLineContainer()
KLineContainer.get(exchange, instrument_id, style)
KLineContainer.set(exchange, instrument_id, style, data)
KLineContainer.init(exchange, instrument_id, style)
KLineProducer()
KLineProducer.update(kline)
KLineProducer.append_data(kline)
KLineProducer.insert_data(kline, index=-1)
KLineProducer.update_last_kline(kline)
KLineProducer.worker()
isdigit()
split_arbitrage_code()
KLineGenerator.exchange  # 属性
KLineGenerator.instrument_id  # 属性
KLineGenerator.style  # 属性
KLineGenerator.producer  # 属性
KLineProducer.exchange  # 属性
KLineProducer.instrument_id  # 属性
KLineProducer.style  # 属性
KLineProducer.kline_container  # 属性
KLineProducer.open  # 属性
KLineProducer.close  # 属性
KLineProducer.high  # 属性
KLineProducer.low  # 属性
KLineProducer.volume  # 属性
KLineProducer.datetime  # 属性
```

