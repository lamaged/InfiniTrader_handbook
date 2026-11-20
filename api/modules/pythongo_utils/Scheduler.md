---
title: "Scheduler"
module: "pythongo.utils"
kind: "function"
import: "from pythongo.utils import Scheduler"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#scheduler"
---


# `Scheduler`


- 模块: `pythongo.utils`  ·  整页: [modules/pythongo_utils](../../../docs/modules/pythongo_utils.md#scheduler)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#scheduler)
- `from pythongo.utils import Scheduler`

简易定时器

通过使用 `apscheduler` 中的 `BackgroundScheduler`（非阻塞定时器），实现一些必要的功能和语法糖，既可以统一定时器的使用规则，还方便用户理解。

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `scheduler_name` | `str` | 定时器名称 | None |

如果传入定时器名称, 则后续实例化同一定时器名称的类时, 都将返回同一内存地址的实例，此为**单例模式**

这样可以让你在不同的策略或实例中管理同一个定时器。

**成员 6 项**：[add_job](Scheduler.add_job.md)、[get_job](Scheduler.get_job.md)、[get_jobs](Scheduler.get_jobs.md)、[remove_job](Scheduler.remove_job.md)、[start](Scheduler.start.md)、[stop](Scheduler.stop.md)
