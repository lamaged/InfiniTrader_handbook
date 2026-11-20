---
title: "Scheduler.add_job"
module: "pythongo.utils"
kind: "function"
scope: "Scheduler"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#scheduler-add_job"
---


# `Scheduler.add_job`


- 模块: `pythongo.utils` › `Scheduler`  ·  [类总览](Scheduler.md)  ·  [整页](../../../docs/modules/pythongo_utils.md#scheduler-add_job)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#scheduler-add_job)

添加定时任务

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `func` | `Callable` | 定时任务函数 | 必填 |
| `trigger` | `Literal["date", "interval", "cron"]` | 触发器 | 必填 |
| `id` | `str` | 任务备注 ID（job_id） | None |

触发器 `trigger` 介绍：

- `date`：在某个确定的时间点运行你的任务函数 （只运行一次）
- `interval`：在固定的时间间隔周期性地运行你的任务函数
- `cron`：在一天的某些固定时间点周期性地运行你的任务函数

此方法用法和 `apscheduler` 完全一致，具体使用方法可以[看这里](https://sinhub.cn/2018/11/apscheduler-user-guide/)或者上网搜索，这里就不做过多解释了，因为每个触发器所需要的参数都是不一样的。

这里实现一个最简单的定时器：

```python
from datetime import datetime

from pythongo.utils import Scheduler

scheduler = Scheduler()

scheduler.start()

def foo():
    """任务函数"""
    print("Amazing PythonGO!")

scheduler.add_job(
    func=foo,
    trigger="interval",
    id="foo_print",
    seconds=5,
    next_run_time=datetime.now()
)


scheduler.remove("foo_print")

scheduler.stop()
```
