---
title: "pythongo.option"
section: "modules/pythongo_option"
---

# pythongo.option

原文: https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_option

| 名称 | 类型 | 说明 | 卡片 |
| --- | --- | --- | --- |
| `Option` | class | 该类提供期权扩展功能，可以计算期权希腊值，由于代码陈旧冗长，这里不过多介绍，具体 | [打开](Option.md) |
| `OptionChain` | function | 该类将同一品种下的所有期权合约整合成了期权链，提供了获取标的月份合约、到期日、行 | [打开](OptionChain.md) |
| `OptionChain.option_chain` | attribute | 类型：dict | [打开](OptionChain.option_chain.md) |
| `OptionChain.option_type` | attribute | 类型：Literal["期权", "股票期权", "现货期权"] | [打开](OptionChain.option_type.md) |
| `OptionChain.get_month_contracts` | function | 获取标的月份合约列表，按到期时间排序 | [打开](OptionChain.get_month_contracts.md) |
| `OptionChain.get_expire_dates` | function | 获取标的月份合约的到期日列表，按到期时间排序 | [打开](OptionChain.get_expire_dates.md) |
| `OptionChain.get_strike_prices` | function | 获取行权价列表，升序排列 | [打开](OptionChain.get_strike_prices.md) |
| `OptionChain.get_call_options` | function | 获取看涨期权合约列表，按行权价升序排列 | [打开](OptionChain.get_call_options.md) |
| `OptionChain.get_put_options` | function | 获取看跌期权合约列表，按行权价升序排列 | [打开](OptionChain.get_put_options.md) |
| `OptionChain.get_atm_option` | function | 获取平值期权档位 | [打开](OptionChain.get_atm_option.md) |
