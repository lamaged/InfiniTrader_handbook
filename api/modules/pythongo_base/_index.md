---
title: "pythongo.base"
section: "modules/pythongo_base"
---

# pythongo.base

原文: https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base

| 名称 | 类型 | 说明 | 卡片 |
| --- | --- | --- | --- |
| `inherit` | section | 在 Python 中，子类通过继承语法继承父类后，可以拥有父类的所有属性或方法， | [打开](inherit.md) |
| `BaseParams` | class | 参数映射模型 | [打开](BaseParams.md) |
| `BaseState` | class | 状态映射模型 | [打开](BaseState.md) |
| `BaseStrategy` | class | 策略模板 | [打开](BaseStrategy.md) |
| `BaseStrategy.strategy_id` | attribute | 类型：int | [打开](BaseStrategy.strategy_id.md) |
| `BaseStrategy.strategy_name` | attribute | 类型：str | [打开](BaseStrategy.strategy_name.md) |
| `BaseStrategy.params_map` | attribute | 类型：BaseParams | [打开](BaseStrategy.params_map.md) |
| `BaseStrategy.state_map` | attribute | 类型：BaseState | [打开](BaseStrategy.state_map.md) |
| `BaseStrategy.limit_time` | attribute | 类型：int | [打开](BaseStrategy.limit_time.md) |
| `BaseStrategy.trading` | attribute | 类型：bool | [打开](BaseStrategy.trading.md) |
| `BaseStrategy.class_name` | attribute | 类型：str | [打开](BaseStrategy.class_name.md) |
| `BaseStrategy.exchange_list` | attribute | 类型：list[str] | [打开](BaseStrategy.exchange_list.md) |
| `BaseStrategy.instrument_list` | attribute | 类型：list[str] | [打开](BaseStrategy.instrument_list.md) |
| `BaseStrategy.instance_file` | attribute | 类型：str | [打开](BaseStrategy.instance_file.md) |
| `BaseStrategy.get_params` | function | 获取策略参数 | [打开](BaseStrategy.get_params.md) |
| `BaseStrategy.set_params` | function | 设置策略参数 | [打开](BaseStrategy.set_params.md) |
| `BaseStrategy.update_status_bar` | function | 更新无限易 PythonGO 窗口状态栏显示值 | [打开](BaseStrategy.update_status_bar.md) |
| `BaseStrategy.save_instance_file` | function | 保存实例信息 | [打开](BaseStrategy.save_instance_file.md) |
| `BaseStrategy.load_instance_file` | function | 加载实例文件并对策略设置对应属性 | [打开](BaseStrategy.load_instance_file.md) |
| `BaseStrategy.on_init` | function | 创建实例回调 | [打开](BaseStrategy.on_init.md) |
| `BaseStrategy.on_start` | function | 启动策略回调 | [打开](BaseStrategy.on_start.md) |
| `BaseStrategy.on_stop` | function | 停止策略回调 | [打开](BaseStrategy.on_stop.md) |
| `BaseStrategy.on_tick` | function | 收到行情 tick 推送回调 | [打开](BaseStrategy.on_tick.md) |
| `BaseStrategy.on_contract_status` | function | 合约状态变化回调 | [打开](BaseStrategy.on_contract_status.md) |
| `BaseStrategy.on_cancel` | function | 收到撤单推送回调 | [打开](BaseStrategy.on_cancel.md) |
| `BaseStrategy.on_order_trade` | function | 收到报单成交推送回调 | [打开](BaseStrategy.on_order_trade.md) |
| `BaseStrategy.on_order` | function | 报单变化回调 | [打开](BaseStrategy.on_order.md) |
| `BaseStrategy.on_trade` | function | 报单成交推送回调 | [打开](BaseStrategy.on_trade.md) |
| `BaseStrategy.on_error` | function | 收到报单错误推送回调 | [打开](BaseStrategy.on_error.md) |
| `BaseStrategy.pause_strategy` | function | 暂停策略函数 | [打开](BaseStrategy.pause_strategy.md) |
| `BaseStrategy.output` | function | 输出信息到控制台 | [打开](BaseStrategy.output.md) |
| `BaseStrategy.sub_market_data` | function | 订阅合约行情函数 | [打开](BaseStrategy.sub_market_data.md) |
| `BaseStrategy.unsub_market_data` | function | 取消订阅合约行情函数 | [打开](BaseStrategy.unsub_market_data.md) |
| `BaseStrategy.sync_position` | function | 同步持仓数据函数 | [打开](BaseStrategy.sync_position.md) |
| `BaseStrategy.get_all_position` | function | 获取所有帐号的所有持仓 | [打开](BaseStrategy.get_all_position.md) |
| `BaseStrategy.get_position` | function | 获取持仓数据函数 | [打开](BaseStrategy.get_position.md) |
| `BaseStrategy.send_order` | function | 报单函数（开仓） | [打开](BaseStrategy.send_order.md) |
| `BaseStrategy.auto_close_position` | function | 自动平仓函数（平今优先） | [打开](BaseStrategy.auto_close_position.md) |
| `BaseStrategy.cancel_order` | function | 撤单函数 | [打开](BaseStrategy.cancel_order.md) |
| `BaseStrategy.make_order_req` | function | 发送报单请求函数 | [打开](BaseStrategy.make_order_req.md) |
| `BaseStrategy.get_account_fund_data` | function | 获取账号资金数据函数 | [打开](BaseStrategy.get_account_fund_data.md) |
| `BaseStrategy.get_instrument_data` | function | 获取合约信息函数 | [打开](BaseStrategy.get_instrument_data.md) |
| `BaseStrategy.get_instruments_by_product` | function | 查询指定品种的所有合约信息或者仅合约代码函数 | [打开](BaseStrategy.get_instruments_by_product.md) |
| `BaseStrategy.get_investor_data` | function | 获取投资者信息函数 | [打开](BaseStrategy.get_investor_data.md) |
