---
title: "CustomLogHandler"
module: "pythongo.utils"
kind: "class"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#customloghandler"
---


# `CustomLogHandler`


- 模块: `pythongo.utils`  ·  整页: [modules/pythongo_utils](../../../docs/modules/pythongo_utils.md#customloghandler)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_utils#customloghandler)

自定义日志 Handler

这个类的作用是，当你使用的 Python 库有自己的日志模块，那这个库所打印的消息你是看不到的，因为 PythonGO 的日志是通过传给无限易，然后展示在界面的，最后才存在文件里，并不是普通输出函数的那种标准输入输出模式。所以当遇到这种情况时，可以使用此 `Handler` 来对你使用的库的 `Logger` 新增一个 `Handler`

具体的使用方法可以自行百度，也可以参考定时器（`Scheduler`）的初始化函数中的代码
