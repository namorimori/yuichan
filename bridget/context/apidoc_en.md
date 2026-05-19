# Bridget Standard Library API Reference

Declare `Use the standard library` at the top of your file to enable these functions.

Function call syntax:
- 1 argument: `funcname of arg`
- 2+ arguments: `funcname of arg1 and arg2 and arg3`
- No arguments: `funcname, do it`

```bridget
Use the standard library
>>> sum of 1 and 2 and 3
6
```

---

## 1. Math Functions

### `abs`

- `abs of x` → number (integer if `x` is integer, float if float)

```bridget
>>> abs of -5
5
```

### `sqrt`

Returns the square root as a **float**. Negative input raises an error.

- `sqrt of x` → float

```bridget
>>> sqrt of 9
3.000000
```

### `random`

Returns a random float in `[0, 1)`.

- `random, do it` → float

---

## 2. Arithmetic Functions

`+`, `-`, `*`, `/`, `%` operators are not used. Call these functions instead.
All accept **variadic arguments** or a single array: `sum of [1,2,3]` = `sum of 1 and 2 and 3`.
If any argument is a float the result is a float; all-integer arguments give an integer.

### `sum`
- `sum of x and y and …` → number

### `diff`
Subtracts each subsequent value from the first.
- `diff of x and y and …` → number

```bridget
>>> diff of 10 and 3 and 2
5
```

### `product`
- `product of x and y and …` → number

### `quotient`
Integer inputs use **floor division**. Dividing by zero raises an error.
- `quotient of x and y` → number

```bridget
>>> quotient of 10 and 3
3
>>> quotient of 10.0 and 3.0
3.333333
```

### `remainder`
- `remainder of x and y` → number

```bridget
>>> remainder of 10 and 3
1
```

### `max` / `min`
- `max of x and y and …` → number
- `min of x and y and …` → number

---

## 3. Bitwise Functions

Both operands are cast to integers before the operation.

| Function | Aliases | Operation |
|----------|---------|-----------|
| `bitand` | `band` | AND (`&`) |
| `bitor` | `bor` | OR (`\|`) |
| `bitxor` | `bxor` | XOR (`^`) |
| `bitnot` | `bnot` | NOT (`~`), 1 argument |
| `lshift` | — | left shift (`<<`) |
| `rshift` | — | right shift (`>>`) |

```bridget
>>> bitand of 6 and 3
2
>>> bitor of 4 and 3
7
>>> bitxor of 6 and 3
5
>>> bitnot of 0
-1
>>> lshift of 1 and 4
16
>>> rshift of 16 and 4
1
```

For 32-bit unsigned arithmetic, wrap with `remainder of (lshift of x and n) and 4294967296`.

---

## 4. Type-Check Functions

Returns `Yes` or `No`.

| Function | Returns `Yes` when… |
|----------|---------------------|
| `isbool of x` | `x` is a boolean |
| `isint of x` | `x` is an integer |
| `isfloat of x` | `x` is a float |
| `isstring of x` | `x` is a string |
| `isarray of x` | `x` is an array |
| `isobject of x` | `x` is an object |

```bridget
>>> isint of 42
Yes
>>> isstring of [1, 2, 3]
No
```

---

## 5. Type-Conversion Functions

### `toint`
`Nothing` → `0`; arrays treated as character-code sequences. Error if conversion fails.
- `toint of x` → integer

```bridget
>>> toint of "42"
42
>>> toint of 3.7
3
```

### `tofloat`
- `tofloat of x` → float

### `tostring`
Floats use 6 decimal places: `"3.140000"`.
- `tostring of x` → string

```bridget
>>> tostring of 42
"42"
>>> tostring of 3.14
"3.140000"
```

### `toarray`
Strings → character-code array. Objects → key array.
- `toarray of x` → array

```bridget
>>> toarray of "Hi"
[72, 105]
>>> toarray of {"x": 1, "y": 2}
["x", "y"]
```

---

## 6. Errors

| Error | Condition |
|-------|-----------|
| `mismatch-argument` | Wrong number of arguments |
| `not-negative-number` | `sqrt` received a negative number |
| `division-by-zero` | `quotient` or `remainder` divided by zero |
| `int-conversion` / `float-conversion` | `toint` / `tofloat` conversion failed |
