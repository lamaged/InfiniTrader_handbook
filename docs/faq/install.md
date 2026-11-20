---
title: "安装问题"
url: "https://infinitrader.quantdo.com.cn/pythongo_v2/faq/install"
---

# 安装问题

无法安装新版本 Python

---

从 Python 3.12 开始，只能在 Windows 8.1 及以上系统安装，已经不再支持 Windows 7 等更低的版本，详情查看 [官方文档 - 在 Windows 上使用 Python](https://docs.python.org/zh-cn/3/using/windows.html)

电脑上可以安装多个版本的 Python 吗

---

可以，后续通过 PythonGO 设置手动选择 Python 版本即可

我可以使用 Anaconda 的 Python 吗

---

可以

我可以自己下载最新版本的 Python 安装吗

---

可以，版本大于等于 Python 3.12 即可

ModuleNotFoundError: No module named '...'

---

一般情况是没操作**安装依赖**这一步导致的，这时候只需要执行`安装依赖.exe`文件即可

No module named 'numpy.core._multiarray_umath'

---

- 64 位无限易需要对应 64 位的 Python, 32 位同理
- 重装或者升级 numpy

安装依赖提示: ERROR: TA-Lib-0.4.xxx.whl is not a supported wheel on this platform

---

这是 Python 位数和依赖版本不一致导致的，需要重新检查环境，统一版本

- `win32` 需要 32 位 Python
- `win_amd64` 需要 64 位 Python

开启 PythonGO 之后无限易启动闪退

---

可能 `Path` 环境变量中有某个路径中存在 Python 的 DLL, 解决方法：

1. 先检查**系统变量 - Path** 中的路径，是否包含 `python.dll` 文件，如果包含该文件，则需要删除该路径
2. 最后检查**用户变量 - Path**，看看 Python 的安装目录是否排在第一位
    - 如果不是，则需要手动把 Python 的安装目录调整到第一位
    - 如果没有找到安装路径，则需要重新安装 Python，且严格按照[安装文档](../python_install.md)操作

注意：如何修改环境变量可以自行百度

IndentationError: ...

---

缩进错误，Python 要求使用四个空格作为缩进，可以使用 [Visual Studio Code](https://code.visualstudio.com/) 编辑器来检查缩进错误

No Qt bindings could be found

---

CMD 输入 `pip cache dir`，把返回的目录删除，然后重新[安装依赖](../python_install.md#requirements)

This application failed to start because no Qt platform plugin could be initialized.

---

未正确设置 QT_QPA_PLATFORM_PLUGIN_PATH 环境变量

安装 PyQt5 提示没权限（Permission denied：... d3dcompiler_47.dll）

---

关闭或卸载 360，再重新[安装依赖](../python_install.md#requirements)

ImportError: DLL load failed while importing aggregations: 找不到指定的模块

---

下载并安装微软运行库：[点我下载](https://infinitrader.quantdo.com.cn/docs/tools.html)

*注意：这个报错必须是由于 `pandas` 模块引起的（常见于 Python 3.12 32 位版本），才可以使用此解决方案*
