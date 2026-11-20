---
title: "Scheduler.get_job"
module: "pythongo.utils"
kind: "function"
scope: "Scheduler"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#scheduler-get_job"
---


# `Scheduler.get_job`


- 模块: `pythongo.utils` › `Scheduler`  ·  [类总览](Scheduler.md)  ·  [整页](../../../docs/modules/pythongo_utils.md#scheduler-get_job)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#scheduler-get_job)

根据 `job_id` 获取对应的定时任务

参数：

| 参数名 | 类型 | 描述 | 默认值 |
| --- | --- | --- | --- |
| `job_id` | `str` | 任务备注 ID | 必填 |

返回：

| 类型 | 描述 |
| --- | --- |
| `apscheduler.job.Job` | 定时任务 |
