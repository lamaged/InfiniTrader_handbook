---
title: "pythongo.utils"
section: "modules/pythongo_utils"
---

# pythongo.utils

原文: https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils

| 名称 | 类型 | 说明 | 卡片 |
| --- | --- | --- | --- |
| `CustomLogHandler` | class | 自定义日志 Handler | [打开](CustomLogHandler.md) |
| `Scheduler` | function | 简易定时器 | [打开](Scheduler.md) |
| `Scheduler.add_job` | function | 添加定时任务 | [打开](Scheduler.add_job.md) |
| `Scheduler.get_job` | function | 根据 job_id 获取对应的定时任务 | [打开](Scheduler.get_job.md) |
| `Scheduler.get_jobs` | function | 返回所有定时任务 | [打开](Scheduler.get_jobs.md) |
| `Scheduler.remove_job` | function | 根据 job_id 移除定时任务 | [打开](Scheduler.remove_job.md) |
| `Scheduler.start` | function | 启动定时器 | [打开](Scheduler.start.md) |
| `Scheduler.stop` | function | 停止定时器 | [打开](Scheduler.stop.md) |
| `KLineGeneratorSec` | function | 秒级 K 线生成器 | [打开](KLineGeneratorSec.md) |
| `KLineGeneratorSec.tick_to_kline` | function | 合成秒级 K 线 | [打开](KLineGeneratorSec.tick_to_kline.md) |
| `KLineGenerator` | function | 分钟级 K 线合成 | [打开](KLineGenerator.md) |
| `KLineGenerator.exchange` | attribute | 类型：str | [打开](KLineGenerator.exchange.md) |
| `KLineGenerator.instrument_id` | attribute | 类型：str | [打开](KLineGenerator.instrument_id.md) |
| `KLineGenerator.style` | attribute | 类型：KLineStyleType | [打开](KLineGenerator.style.md) |
| `KLineGenerator.producer` | attribute | 类型：KLineProducer | [打开](KLineGenerator.producer.md) |
| `KLineGenerator.push_history_data` | function | 推送历史 K 线数据到回调 | [打开](KLineGenerator.push_history_data.md) |
| `KLineGenerator.stop_push_scheduler` | function | 停止推送每个交易时段最后一根 K 线的定时器 | [打开](KLineGenerator.stop_push_scheduler.md) |
| `KLineGenerator.tick_to_kline` | function | 合成 K 线 | [打开](KLineGenerator.tick_to_kline.md) |
| `KLineGeneratorArb` | class | 标准套利合约的分钟级 K 线合成器 | [打开](KLineGeneratorArb.md) |
| `KLineContainer` | function | K 线容器 | [打开](KLineContainer.md) |
| `KLineContainer.get` | function | 根据交易所, 合约和 K 线分钟获取缓存的 K 线 | [打开](KLineContainer.get.md) |
| `KLineContainer.set` | function | 根据交易所, 合约和 K 线分钟缓存 K 线 | [打开](KLineContainer.set.md) |
| `KLineContainer.init` | function | 获取合约 K 线并缓存 | [打开](KLineContainer.init.md) |
| `KLineProducer` | function | K 线生产器 | [打开](KLineProducer.md) |
| `KLineProducer.exchange` | attribute | 类型：str | [打开](KLineProducer.exchange.md) |
| `KLineProducer.instrument_id` | attribute | 类型：str | [打开](KLineProducer.instrument_id.md) |
| `KLineProducer.style` | attribute | 类型：KLineStyleType | [打开](KLineProducer.style.md) |
| `KLineProducer.kline_container` | attribute | 类型：KLineContainer | [打开](KLineProducer.kline_container.md) |
| `KLineProducer.open` | attribute | 类型：list[np.float64] | [打开](KLineProducer.open.md) |
| `KLineProducer.close` | attribute | 类型：list[np.float64] | [打开](KLineProducer.close.md) |
| `KLineProducer.high` | attribute | 类型：list[np.float64] | [打开](KLineProducer.high.md) |
| `KLineProducer.low` | attribute | 类型：list[np.float64] | [打开](KLineProducer.low.md) |
| `KLineProducer.volume` | attribute | 类型：list[np.float64] | [打开](KLineProducer.volume.md) |
| `KLineProducer.datetime` | attribute | 类型：list[TypeDateTime] | [打开](KLineProducer.datetime.md) |
| `KLineProducer.update` | function | 更新数据序列 | [打开](KLineProducer.update.md) |
| `KLineProducer.append_data` | function | 添加 K 线数据 | [打开](KLineProducer.append_data.md) |
| `KLineProducer.insert_data` | function | 根据数组下标插入 K 线数据 | [打开](KLineProducer.insert_data.md) |
| `KLineProducer.update_last_kline` | function | 更新最后一根 K 线数据 | [打开](KLineProducer.update_last_kline.md) |
| `KLineProducer.worker` | function | 将 K 线数据转成 K 线对象后更新到本实例中的 K 线数据序列，并且推送到 K | [打开](KLineProducer.worker.md) |
| `isdigit` | function | 判断字符串是否整数或小数 | [打开](isdigit.md) |
| `split_arbitrage_code` | function | 分割套利合约代码 | [打开](split_arbitrage_code.md) |
