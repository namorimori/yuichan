# Yui Language Specification

Yui is a Japanese-syntax educational programming language.
It uses natural Japanese word order and minimal symbols so programs can
be read and written by beginners.

---

## 1. Lexical Rules

The minimal units (tokens) that make up a Yui source file.

| Element | Details |
|---------|---------|
| Whitespace | space, tab, fullwidth space `　` |
| Newline | `\n` (statement separator) |
| Line comment | `#` or `＃` to end of line |
| Identifier | `/[A-Za-z_][A-Za-z0-9_]*/`, or any sequence wrapped in `「…」` |

One statement per line is the norm.
Variable names may be Japanese words (`絶対値`, `最大値`) or ASCII identifiers.

---

## 2. Type System

Every value belongs to exactly one of seven types.

| Type | Literal |
|------|---------|
| Null | `値なし` |
| Boolean | `真` / `偽` |
| Integer | `42` |
| Float | `3.14` (displayed with 6 decimal places) |
| String | `"あ"`, `"x={x}"` |
| Array | `[1, 2, 3]` |
| Object | `{"x": 1, "y": 2}` |

- **Strings** are stored internally as **character-code (int) arrays**. This means strings and arrays share the same operations (append, length, indexing).
- **Integers** are stored internally as **bit arrays (LSB first)**. Therefore all array operations (indexing, length, append) implicitly apply to integers too (e.g. `6` behaves as `[0,1,1]`; `6[0]` = `0`, `6[1]` = `1`, `6の大きさ` = `3`). This lets you implement bit operations as pure array manipulation.
- Array equality is recursive. A character-code array and its string compare equal (`[72,105]` == `"Hi"`), and a bit array and its integer compare equal (`[0,1,1]` == `6`).

---

## 3. Expressions

Constructs that produce a value. Expressions may be freely nested.

### 3.1 Literals

| Type | Literal |
|------|---------|
| Null | `値なし` |
| Boolean | `真` / `偽` |
| Integer | `42` |
| Float | `3.14` (6 decimal places when displayed) |
| String | `"あ"` |
| Array | `[1, 2, 3]` |
| Object | `{"x": 1, "y": 2}` |

### 3.2 String Interpolation

Embed an expression inside a string with `{expr}`.

```
name = "ゆい"
msg  = "こんにちは、{name}さん"
```

Escape `{` as `\{` and `"` as `\"`. `\\`, `\n`, `\t` are also supported.

### 3.3 Length

```
exprの大きさ
```

Returns the number of elements in an array or string.

### 3.4 Unary Minus

`-expr` negates a numeric value. May be written directly on a literal: `y = -2`.

### 3.5 Arithmetic

Yui uses **no arithmetic symbols** (`+`, `-`, `*`, `/`, `%`).
Use standard-library functions instead.

| Function | Meaning |
|----------|---------|
| `和(x, …)` | sum (array argument also accepted) |
| `差(x, y, …)` | difference |
| `積(x, y, …)` | product |
| `商(x, y)` | quotient (floor division for integers) |
| `剰余(x, y)` | remainder |

### 3.6 Indexing / Properties

- `a[i]` — element at index `i` of array `a` (0-based)
- `O["x"]` — property `"x"` of object `O`
- `aの大きさ` — number of elements in array or string `a`

```
A = [10, 20, 30]
A[1] = 200        # write to index

O = {"x": 0, "y": 0}
O["x"] = 1        # write to property
```

### 3.7 Function Application

```
f(a, b, c)
```

Arguments are separated by `,`.

---

## 4. Statements

### 4.1 Assignment

```
x = expr
```

Re-assigning overwrites the previous value.

### 4.2 Increment / Decrement

```
xを増やす
xを減らす
```

Both change the variable by exactly 1. Also works on indexed positions: `A[0]を増やす`.

### 4.3 Append

```
aにxを追加する
```

Appends `x` to the end of array `a`. Strings accept appending character codes.

### 4.4 Conditional

```
もしxがyならば {
   …
}
そうでなければ {
   …
}
```

`そうでなければ` is optional. For elif-style chains, nest `もし` inside `そうでなければ`.

#### Comparison Suffixes

`==`, `!=`, `<`, `>`, `<=`, `>=` **symbols are not used**. Write `もし A が B <suffix> ならば`:

| Suffix | Operator | Example |
|--------|----------|---------|
| (none) | `==` | `もしxが0ならば` |
| `以外` | `!=` | `もしxが0以外ならば` |
| `より小さい` | `<` | `もしrがbより小さいならば` |
| `より大きい` | `>` | `もしxが10より大きいならば` |
| `以下` | `<=` | `もしdistが1以下ならば` |
| `以上` | `>=` | `もしnが100以上ならば` |
| `のいずれか` | `in` | `もし"banana"がfruitsのいずれかならば` |
| `のいずれでもない` | `not in` | `もし"grape"がfruitsのいずれでもないならば` |

#### Multi-way Branching

Yui has no `elif`. Nest `もし` inside `そうでなければ`.

### 4.5 Repeat

```
N回くり返す {
   …
}
```

Exit early with `くり返しを抜ける`.

### 4.6 Function Definition

```
f = 入力 x, y に対し {
   …
   expr が答え
}
```

- No parameters: `入力なしに対し { … }`
- Return a value: `expr が答え`
- Return without value: `関数から抜ける`
- Variables defined inside a function are **local** and invisible outside.
- **Implicit return**: if the body ends without `が答え` or `関数から抜ける`, the runtime returns an object containing all local variables.

```
point = 入力x,yに対し{
   # no explicit return → returns {"x": x, "y": y}
}
O = point(3, 5)
>>> O["x"]
3
```

### 4.7 Doctest (Assert)

```
>>> expr
expected_literal
```

Evaluates `expr` and asserts it equals the literal. Follows Python doctest convention.

### 4.8 Import

```
標準ライブラリを使う
```

Registers all standard library functions. Must appear before any call to those functions.

### 4.9 Pass

```
何もしない
```

### 4.10 Print Expression

A standalone expression evaluates and prints its result automatically.

---

## 5. Blocks

Blocks are delimited by `{ … }`. Standard indentation is three spaces per nesting level.

| Construct | Opens with | Closes with |
|-----------|------------|-------------|
| If | `もし…ならば` | `}` |
| Else | `そうでなければ` | `}` |
| Loop | `N回くり返す` | `}` |
| Function | `NAME = 入力PARAMS に対し` | `}` |

---

## 6. Standard Library (Summary)

Declare `標準ライブラリを使う` to enable these functions.

| Category | Functions |
|----------|-----------|
| Math | `絶対値(x)` · `平方根(x)` · `乱数()` |
| Arithmetic | `和` · `差` · `積` · `商` · `剰余` · `最大値` · `最小値` |
| Convert | `整数化(x)` · `小数化(x)` · `文字列化(x)` · `配列化(x)` |
| Type check | `ブール判定(x)` · `整数判定(x)` · `小数判定(x)` · `文字列判定(x)` · `配列判定(x)` · `オブジェクト判定(x)` |

See `apidoc_en.md` for full signatures and examples.
