---
title: "pythongo.types"
url: "https://infinitrader.quantdo.com.cn/pythongo_v2/modules/pythongo_types"
---

# pythongo.types

<a id="typedatetime"></a>
## `TypeDateTime`

时间类型，等同于 `datetime.datetime`

<a id="typeproduct"></a>
## `TypeProduct`

品种类型

```python
Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "h"]
```

对应关系请查看 [数值映射 - ProductClassType](../faq/mapping.md#productclasstype)

<a id="typeinstresult"></a>
## `TypeInstResult`

合约信息数据类型

```python
dict[TypeProduct, list[InstrumentData | str]]
```

<a id="typeorderdir"></a>
## `TypeOrderDIR`

报单方向

```python
Literal["buy", "sell"]
```

对应关系如下

| 键 | 值 |
| --- | --- |
| "buy" | 买 |
| "sell" | 卖 |

<a id="typehedgeflag"></a>
## `TypeHedgeFlag`

投机套保标志

```python
Literal["1", "2", "3", "4", "5", "6", "7"]
```

> [!WARNING]
> `6` 和 `7` 只支持上期所和能源中心。

对应关系请查看 [数值映射 - HedgeFlagType](../faq/mapping.md#hedgeflagtype)

<a id="typeorderflag"></a>
## `TypeOrderFlag`

报单指令

```python
Literal["GFD", "FAK", "FOK"]
```

指令解释[看这里](https://infinitrader.quantdo.com.cn/docs/explanation.html)

<a id="typeraworderflag"></a>
## `TypeRAWOrderFlag`

原始报单指令

```python
Literal["0", "1", "2"]
```

和上方报单指令相对应，如果使用 `infini.send_order` 函数，则使用此类型

<a id="typeoffsetflag"></a>
## `TypeOffsetFlag`

开平标志

```python
Literal["0", "1", "3", "g", "h", "i", "j", "k", "l"]
```

对应关系请查看 [数值映射 - OffsetFlagType](../faq/mapping.md#offsetflagtype)
