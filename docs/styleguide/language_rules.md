---
title: "语言规范"
url: "https://infinitrader.quantdo.com.cn/pythongo_v2/styleguide/language_rules"
---

# 语言规范

任何代码语言都有代码规范，有了规范才能让我们写出清晰易读易懂的代码，以下列出 PythonGO 的语言规范，实际上就是 Python 的语言规范。

> [!NOTE]
> 代码编辑器统一使用 [Visual Studio Code](https://code.visualstudio.com/download)

<a id="import"></a>
## 导入

正常情况下，导包使用 `import` 语句

```python
import pythongo

pythongo.utils.KLineGenerator(...)
```

可以适当使用 `from` 语句来省略太长的包名

```python
from pythongo import utils

utils.KLineGenerator(...)
```

或者直接导入包中的对象

```python
from pythongo.utils import KLineGenerator

KLineGenerator(...)
```

<a id="import-sort"></a>
### 导入顺序

按照如下导入顺序来编写你的 `import` 语句， 标准库 -> 第三方库 -> 本地库，例如：

```python
# 标准库
import os
from datetime import datetime

# 第三方库
import requests

# 本地库
import pythongo
```

<a id="import-tips"></a>
### 注意事项

严格禁止使用星号 `*` 导入

```python
from pythongo import *
```

缩写导入只适用于库的缩写是约定俗成的，比如 `numpy` 和 `pandas`，其他所有库都不建议使用缩写导入

```python
import numpy as np
import pandas as pd
```

<a id="exception"></a>
## 异常

任何报错都有解决方法，对于 `try / except` 语句要严格控制使用频率。

<a id="true-false-condition"></a>
## True / False 的求值

Python 在计算布尔值时会把一些值视为 `False`。简单来说，所有的「空」值都是假值。 因此， `0, None, [], {}, ""` 作为布尔值使用时相当于 `False`

当我们判断一个值 `foo` 是否为 `True` 或者 `False` 时，可以直接使用 `if foo:`

但是当值 `foo` 可能为 `None` 值时，一定要使用 `if foo is None:`（或者 `is not None`）来判断 `None` 值，因为在某些情况下，`0` 值并不代表 `False`

当你想条件为 `False` 时进入判断，应该写成

```python
if foo is False:
    # do something
```

因为这样明确了当 `foo` 值或结果为 `False` 时才进入 `if` 判断，不会造成歧义。

<a id="type-hints"></a>
## 类型注释

由于 Python 是动态语言，一个变量被赋值后，运行时可以改变该变量的类型，所以有时候当变量的类型被改变后，我们的编辑器不能识别该变量的类型，导致无法使用编辑器的函数自动补全功能。

而在新版本的 Python 中，我们可以通过类型注释来实现给每个变量定义一个类型，提高代码可读性和可维护性。

以下代码告诉我们 `foo` 函数需要传入两个 `int` 类型的参数 `a` 和 `b`，函数返回的结果也是 `int` 类型

```python
def foo(a: int, b: int) -> int:
    return a + b
```

编写类型注释是一个非常好的习惯，更具体的类型注释文档可以查看 [官方文档 - 对类型提示的支持](https://docs.python.org/zh-cn/3/library/typing.html)，或者网上搜索相关内容。
