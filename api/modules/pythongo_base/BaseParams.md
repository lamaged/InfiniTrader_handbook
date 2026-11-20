---
title: "BaseParams"
module: "pythongo.base"
kind: "class"
import: "from pythongo.base import BaseParams"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#baseparams"
---


# `BaseParams`


- 模块: `pythongo.base`  ·  整页: [modules/pythongo_base](../../../docs/modules/pythongo_base.md#baseparams)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#baseparams)
- `from pythongo.base import BaseParams`

参数映射模型

定义好的映射关系，会展示在「PythonGO 窗口 - 参数」一栏，这样就可以在界面直接编辑参数

默认定义了 `exchange`（交易所代码） 和 `instrument_id`（合约代码），这两个参数是固定参数，在继承本类后，你可以不再定义这两个参数，但建议还是**显式**的定义这两个参数。
