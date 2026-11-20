---
title: "inherit"
module: "pythongo.base"
kind: "section"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#inherit"
---


# `inherit`


- 模块: `pythongo.base`  ·  整页: [modules/pythongo_base](../../../docs/modules/pythongo_base.md#inherit)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_base#inherit)

在 Python 中，子类通过继承语法继承父类后，可以拥有父类的所有属性或方法，这样极大的减少了重复的代码，可以让代码更加简洁高效。

当我们继承父类后，拥有了父类的所有属性和方法，有时候我们需要对该父类的一些方法进行重写，但同时还需要继续使用父类的方法，这个时候就需要使用 `super()` 函数了。

因为我们对该方法重写后，再使用 `self.method_name()` 准备调用父类的方法，会发现其实调用的还是自身类（子类）的方法，也就是你自己重写后的方法，这个时候需要使用 `super().method_name()` 来调用父类的同名方法，就能达到我们想要的效果了。

具体的继承概念可以自行查阅互联网资料。
