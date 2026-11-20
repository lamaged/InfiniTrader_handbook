---
title: "get_position"
module: "examples"
kind: "recipe"
source: "https://infinitrader.quantdo.com.cn/pythongo_v2/examples#get_position"
---


# `get_position`


- 模块: `examples`  ·  整页: [examples](../../docs/examples.md#get_position)  ·  [原文](https://infinitrader.quantdo.com.cn/pythongo_v2/examples#get_position)

查询 `ag2602` 的持仓

```python
class Demo(...):
    def on_start(self) -> None:
        super().on_start()

        position = self.get_position("ag2602")

        position.position

        position.net_position

        position.long.position

        position.short.td_position_close

        position.short.yd_position_close

        position.long.open_volume

        position.long.close_volume

        short_position = self.get_position("ag2602").get_single_position("short")
        short_position.position # 空头总持仓

        position = self.get_position("ag2602", hedgeflag="3")
        position.long.position # 套保多头总持仓

        position = self.get_position("ag2602", investor="888888")
        position.position # 指定帐号总持仓

        position = self.get_position("ag2602", simple=True)
        position.position # 该持仓会在报单成交后立刻更新
```

---

获取全部持仓（仅 `v2025.1112` 之后版本可用）

```python
class Demo(...):
    def on_start(self) -> None:
        super().on_start()

        position = self.get_all_position()  # 所有帐号所有合约的所有持仓
        position["888888"]  # 888888 帐号的全部持仓数据
        position["888888"]["ag2602"]  # 888888 帐号下 ag2602 的全部持仓数据
        position["888888"]["ag2602"]["3"]  # 888888 帐号下 ag2602 的套保持仓数据
        position["888888"]["ag2602"]["1"].long  # 888888 帐号下 ag2602 的多头持仓数据
```
