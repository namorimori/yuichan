# Yui Standard Library API Reference

Declare `標準ライブラリを使う` at the top of your program to enable these functions.
All functions are called as `name(args)`.

```yui
標準ライブラリを使う
>>> 和(1, 2, 3)
6
```

---

## 1. Math Functions

### 絶対値

Returns the absolute value of a number. Integer in → integer out; float in → float out.

- `絶対値(x)` → number

```yui
>>> 絶対値(-5)
5
```

### 平方根

Returns the square root as a **float**. Negative input raises an error.

- `平方根(x)` → float

```yui
>>> 平方根(9)
3.000000
```

### 乱数

Returns a random float in `[0, 1)`. No arguments.

- `乱数()` → float

---

## 2. Arithmetic Functions

`+`, `-`, `*`, `/`, `%` operators are not used in Yui. Call these functions instead.
All accept **variadic arguments** or a single array:
`和([1,2,3])` = `和(1,2,3)`.
If any argument is a float the result is a float; all-integer arguments give an integer.

### 和

Sum of all arguments.

- `和(x, y, …)` → number

```yui
>>> 和(1, 2, 3)
6
>>> 和([1, 2, 3])
6
```

### 差

Subtracts each subsequent value from the first.

- `差(x, y, …)` → number

```yui
>>> 差(10, 3, 2)
5
```

### 積

Product of all arguments.

- `積(x, y, …)` → number

### 商

Integer inputs use **floor division**. Dividing by zero raises an error.

- `商(x, y)` → number

```yui
>>> 商(10, 3)
3
>>> 商(10.0, 3.0)
3.333333
```

### 剰余

- `剰余(x, y)` → number

```yui
>>> 剰余(10, 3)
1
```

### 最大値 / 最小値

- `最大値(x, y, …)` → number (array argument also accepted)
- `最小値(x, y, …)` → number (array argument also accepted)

---

## 3. Type-Check Functions

Returns `真` or `偽`.

| Function | Returns `真` when… |
|----------|--------------------|
| `ブール判定(x)` | x is a boolean |
| `整数判定(x)` | x is an integer |
| `小数判定(x)` | x is a float |
| `文字列判定(x)` | x is a string |
| `配列判定(x)` | x is an array |
| `オブジェクト判定(x)` | x is an object |

```yui
標準ライブラリを使う
>>> 整数判定(42)
真
>>> 文字列判定([1,2,3])
偽
```

---

## 4. Type-Conversion Functions

### 整数化

`値なし` → `0`; arrays treated as character-code sequences. Error if conversion fails.

- `整数化(x)` → integer

```yui
>>> 整数化("42")
42
>>> 整数化(3.7)
3
```

### 小数化

- `小数化(x)` → float

```yui
>>> 小数化(5)
5.000000
```

### 文字列化

Floats use 6 decimal places: `"3.140000"`.

- `文字列化(x)` → string

```yui
>>> 文字列化(42)
"42"
>>> 文字列化(3.14)
"3.140000"
```

### 配列化

Strings → character-code array. Objects → key array.

- `配列化(x)` → array

```yui
>>> 配列化("Hi")
[72, 105]
>>> 配列化({"x": 1, "y": 2})
["x", "y"]
```

---

## 5. Errors

| Error | Condition |
|-------|-----------|
| `mismatch-argument` | Wrong number of arguments |
| `not-negative-number` | `平方根` received a negative number |
| `division-by-zero` | `商` or `剰余` divided by zero |
| `int-conversion` / `float-conversion` | `整数化` / `小数化` conversion failed |

---

## 6. Quick Reference

| Category | Function | Call form |
|----------|----------|-----------|
| Math | 絶対値 | `絶対値(x)` |
| Math | 平方根 | `平方根(x)` |
| Math | 乱数 | `乱数()` |
| Arithmetic | 和 | `和(x, y, …)` |
| Arithmetic | 差 | `差(x, y, …)` |
| Arithmetic | 積 | `積(x, y, …)` |
| Arithmetic | 商 | `商(x, y)` |
| Arithmetic | 剰余 | `剰余(x, y)` |
| Arithmetic | 最大値 | `最大値(x, y, …)` |
| Arithmetic | 最小値 | `最小値(x, y, …)` |
| Type check | ブール判定 | `ブール判定(x)` |
| Type check | 整数判定 | `整数判定(x)` |
| Type check | 小数判定 | `小数判定(x)` |
| Type check | 文字列判定 | `文字列判定(x)` |
| Type check | 配列判定 | `配列判定(x)` |
| Type check | オブジェクト判定 | `オブジェクト判定(x)` |
| Convert | 整数化 | `整数化(x)` |
| Convert | 小数化 | `小数化(x)` |
| Convert | 文字列化 | `文字列化(x)` |
| Convert | 配列化 | `配列化(x)` |
