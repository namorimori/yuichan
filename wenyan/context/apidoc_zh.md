# Wenyan Standard Library API Reference

Declare `引標準庫` at the top of your program to enable these functions.

Function call syntax:
- 1 argument: `施FUNC於x`
- 2+ arguments: `施FUNC於x與y與z`
- No arguments: `施FUNC以虛`

```wenyan
引標準庫
>>> 施和於1與2與3
6
```

---

## 1. Math Functions

### 絶対値

Returns the absolute value of a number. Integer in → integer out; float in → float out.

- `施絶対値於x` → number

```wenyan
>>> 施絶対値於-5
5
```

### 平方根

Returns the square root as a **float**. Negative input raises an error.

- `施平方根於x` → float

```wenyan
>>> 施平方根於9
3.000000
```

### 乱数

Returns a random float in `[0, 1)`. No arguments.

- `施乱数以虛` → float

---

## 2. Arithmetic Functions

`+`, `-`, `*`, `/`, `%` operators are not used in wenyan. Call these functions instead.
All accept **variadic arguments** or a single array:
`施和於[1,2,3]` = `施和於1與2與3`.
If any argument is a float the result is a float; all-integer arguments give an integer.

### 和

Sum of all arguments.

- `施和於甲與乙與…` → number

```wenyan
>>> 施和於1與2與3
6
>>> 施和於[1,2,3]
6
```

### 差

Subtracts each subsequent value from the first.

- `施差於甲與乙與…` → number

```wenyan
>>> 施差於10與3與2
5
```

### 積

Product of all arguments.

- `施積於甲與乙與…` → number

### 商

Integer inputs use **floor division**. Dividing by zero raises an error.

- `施商於甲與乙` → number

```wenyan
>>> 施商於10與3
3
>>> 施商於10.000000與3.000000
3.333333
```

### 剰余

- `施剰余於甲與乙` → number

```wenyan
>>> 施剰余於10與3
1
```

### 最大値 / 最小値

- `施最大値於甲與乙與…` → number (array argument also accepted)
- `施最小値於甲與乙與…` → number (array argument also accepted)

---

## 3. Type-Check Functions

Returns `然` or `否`.

| Function call | Returns `然` when… |
|---------------|--------------------|
| `施真偽判定於x` | x is a boolean |
| `施整数判定於x` | x is an integer |
| `施小数判定於x` | x is a float |
| `施文字列判定於x` | x is a string |
| `施配列判定於x` | x is an array |
| `施オブジェクト判定於x` | x is an object |

```wenyan
引標準庫
>>> 施整数判定於42
然
>>> 施文字列判定於[1,2,3]
否
```

---

## 4. Type-Conversion Functions

### 整数化

`無` → `0`; arrays treated as character-code sequences. Error if conversion fails.

- `施整数化於x` → integer

```wenyan
>>> 施整数化於「42」
42
>>> 施整数化於3.700000
3
```

### 小数化

- `施小数化於x` → float

```wenyan
>>> 施小数化於5
5.000000
```

### 文字列化

Floats use 6 decimal places: `「3.140000」`.

- `施文字列化於x` → string

```wenyan
>>> 施文字列化於42
「42」
>>> 施文字列化於3.140000
「3.140000」
```

### 配列化

Strings → character-code array. Objects → key array.

- `施配列化於x` → array

```wenyan
>>> 施配列化於「Hi」
[72, 105]
>>> 施配列化於{"x": 1, "y": 2}
[「x」, 「y」]
```

---

## 5. Quick Reference

| Category | Function | Call form |
|----------|----------|-----------|
| Math | 絶対値 | `施絶対値於x` |
| Math | 平方根 | `施平方根於x` |
| Math | 乱数 | `施乱数以虛` |
| Arithmetic | 和 | `施和於x與y` |
| Arithmetic | 差 | `施差於x與y` |
| Arithmetic | 積 | `施積於x與y` |
| Arithmetic | 商 | `施商於x與y` |
| Arithmetic | 剰余 | `施剰余於x與y` |
| Arithmetic | 最大値 | `施最大値於x與y` |
| Arithmetic | 最小値 | `施最小値於x與y` |
| Type check | 真偽判定 | `施真偽判定於x` |
| Type check | 整数判定 | `施整数判定於x` |
| Type check | 小数判定 | `施小数判定於x` |
| Type check | 文字列判定 | `施文字列判定於x` |
| Type check | 配列判定 | `施配列判定於x` |
| Type check | オブジェクト判定 | `施オブジェクト判定於x` |
| Convert | 整数化 | `施整数化於x` |
| Convert | 小数化 | `施小数化於x` |
| Convert | 文字列化 | `施文字列化於x` |
| Convert | 配列化 | `施配列化於x` |

---

## 6. Errors

| Error | Condition |
|-------|-----------|
| `mismatch-argument` | Wrong number of arguments |
| `not-negative-number` | `平方根` received a negative number |
| `division-by-zero` | `商` or `剰余` divided by zero |
| `int-conversion` / `float-conversion` | `整数化` / `小数化` conversion failed |
