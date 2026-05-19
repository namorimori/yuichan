# Wenyan Language Specification

Wenyan (文言) is a Classical Chinese dialect of the Yui programming language.
Programs are written using Classical Chinese phrases and CJK characters.
All mathematical symbols and operators are replaced by Chinese words or
standard-library function calls.

---

## 1. Lexical Elements

The minimal units (tokens) that make up a wenyan source file.

| Element | Details |
|---------|---------|
| Whitespace | space, tab, fullwidth space `　` |
| Newline | `\n` (statement separator) |
| Line comment | `注` (optionally `注、` or `注。`) to end of line |
| Identifier | ASCII `/[A-Za-z_][A-Za-z0-9_]*/`, or any non-whitespace/non-punctuation sequence, or backtick-wrapped `` `…` `` |

One statement per line is the norm.
Variable names may be single CJK characters (`甲`, `乙`, `丙`, …) or
multi-character words (`結果`, `計數`, …).

---

## 2. Type System

Every value belongs to exactly one of seven types.

| Type | Literal |
|------|---------|
| Null | `無` |
| Boolean | `然` / `否` |
| Integer | `42` |
| Float | `3.14` (displayed with 6 decimal places) |
| String | `「hello」`, `「x={x}」` |
| Array | `[1, 2, 3]` |
| Object | `{"x": 1, "y": 2}` |

- Strings are stored internally as **character-code (int) arrays**. This means
  strings and arrays share the same operations (append, length, indexing).
- Integers are stored internally as **bit arrays (LSB first)**. Therefore all
  array operations (indexing, length, append) implicitly apply to integers too
  (e.g. `6` behaves as `[0,1,1]`; `取6之第0` = `0`, `取6之第1` = `1`,
  `6之量` = `3`). This lets you implement bit operations (NOT, AND, OR, XOR,
  shift, add) as pure array manipulation.
- Array equality is recursive. A character-code array and its string compare
  equal (`[72,105]` == `「Hi」`), and a bit array and its integer compare equal
  (`[0,1,1]` == `6`).

---

## 3. Expressions

Constructs that produce a value. Expressions may be freely nested.

### 3.1 Literals

| Type | Literal |
|------|---------|
| Null | `無` |
| Boolean | `然` / `否` |
| Integer | `42` |
| Float | `3.14` (6 decimal places when displayed) |
| String | `「hello」` |
| Array | `[1, 2, 3]` |
| Object | `{"x": 1, "y": 2}` |

### 3.2 String Interpolation

Embed an expression inside a string with `{expr}`.

```
吾有一數、曰「Alice」、名之曰名。
吾有一數、曰「こんにちは、{名}さん」、名之曰訊。
```

Escape `{` as `\{`. `\\`, `\n`, `\t` are also supported.

### 3.3 Length

```
EXPR之量
```

Returns the number of elements in an array or string.

### 3.4 Unary Minus

`-EXPR` negates a numeric value. May be written directly on a literal:
`吾有一數、曰-2、名之曰乙。`

### 3.5 Arithmetic

Wenyan uses **no arithmetic symbols** (`+`, `-`, `*`, `/`, `%`).
Use standard-library functions instead.

| Function call | Meaning |
|---------------|---------|
| `施和於甲與乙` | sum (variadic / array accepted) |
| `施差於甲與乙` | difference |
| `施積於甲與乙` | product (variadic / array accepted) |
| `施商於甲與乙` | quotient (floor division for integers) |
| `施剰余於甲與乙` | remainder |

### 3.6 Indexing / Properties

Read an element with `取ARRAY之第INDEX`.

```
吾有一數、曰取甲之第0、名之曰首。      注 read甲[0]
吾有一數、曰取O之第「x」、名之曰x値。   注 read O["x"]
```

To write to an indexed position, use the index expression as the assignment name:

```
吾有一數、曰200、名之曰取甲之第1。     注 甲[1] = 200
```

### 3.7 Function Application

```
施FUNC於ARG1與ARG2        # two arguments
施FUNC於ARG1與ARG2與ARG3  # three arguments
施FUNC以虛                 # zero arguments
```

Nested calls:

```
施積於n與(施階乗於(施差於n與1))
```

---

## 4. Statements

Execution units that update variables and control flow.

### 4.1 Assignment

Bind a value to a name. Re-assigning overwrites the previous value.
**Value is written before name** — the reverse of most languages.

```
吾有一數、曰EXPR、名之曰NAME。
```

To write to an indexed position, use the index expression as NAME:

```
吾有一數、曰0、名之曰取甲之第2。    注 甲[2] = 0
```

### 4.2 Increment / Decrement

Change a numeric variable by exactly 1.

```
增NAME以一。
減NAME以一。
```

Also works on indexed positions:

```
增取甲之第0以一。    注 甲[0] += 1
```

### 4.3 Append

Append one value to the end of an array.

```
納EXPR入ARRAY。
```

Strings accept appending character codes in the same way.

### 4.4 Conditional

```
若CONDITION乎、則
   …
條畢。

若CONDITION乎、則
   …
否則
   …
條畢。
```

`否則` is optional. For elif-style chains, nest `若` inside `否則`.

#### Comparison Keywords

`==`, `!=`, `<`, `>`, `<=`, `>=` **symbols are not used**.

| Keyword | Meaning | Example |
|---------|---------|---------|
| `等於` | `==` | `若x等於0乎、則` |
| `異於` | `!=` | `若x異於0乎、則` |
| `小於` | `<` | `若r小於b乎、則` |
| `大於` | `>` | `若x大於10乎、則` |
| `不大於` | `<=` | `若i不大於n乎、則` |
| `不小於` | `>=` | `若n不小於100乎、則` |
| `含` | `in` | `若「banana」含果乎、則` |
| `不含` | `not in` | `若「grape」不含果乎、則` |

#### Multi-way Branching

Wenyan has no `elif`. Nest `若` inside `否則`.

### 4.5 Repeat

Execute a block a given number of times. Exit early with `止。`.

```
N度、
   …
度畢。
```

### 4.6 Function Definition

```
術曰NAME以PARAM1與PARAM2…
   …
   以EXPR答。
術畢。
```

Zero-parameter functions use `術曰NAME。`:

```
術曰招呼。
   以「你好！」答。
術畢。
```

- **Return a value**: `以EXPR答。`
- **Return without value**: `還無。`
- Variables defined inside a function are **local** and invisible outside.
- **Implicit return**: if the body ends without `以...答。` or `還無。`, the runtime
  returns an object containing all local variables (constructor-like pattern).

### 4.7 Doctest (Assert)

```
>>> EXPR
expected_literal
```

Evaluates `EXPR` and asserts it equals the literal (Python doctest convention).
Function calls in doctest lines use wenyan syntax:

```
>>> 施和於3與4
7
```

### 4.8 Import

```
引標準庫
```

Registers all standard library functions in the current environment.
Must appear before any stdlib call.

### 4.9 Pass

```
無為。
```

A no-op placeholder.

### 4.10 Print Expression

A standalone expression evaluates and prints its result automatically (REPL-like).
`吿曰EXPR。` is the explicit print statement.

---

## 5. Blocks

A block is a sequence of statements.
Wenyan uses structural keywords as delimiters — no braces or indentation rules.
The standard indentation is three spaces per level (convention, not enforced).

| Construct | Opener | Terminator |
|-----------|--------|-----------|
| If | `若…乎、則` | `條畢。` |
| Else | `否則` | (same `條畢。`) |
| Loop | `N度、` | `度畢。` |
| Function (with args) | `術曰NAME以PARAMS` | `術畢。` |
| Function (no args) | `術曰NAME。` | `術畢。` |

---

## 6. Standard Library (Summary)

Declare `引標準庫` to enable these functions.

| Category | Functions |
|----------|-----------|
| Math | `施絶対値於x` · `施平方根於x` · `施乱数以虛` |
| Arithmetic | `施和/差/積/商/剰余於甲與乙` · `施最大値/最小値於甲與乙` |
| Convert | `施整数化/小数化/文字列化/配列化於x` |
| Type check | `施整数判定/小数判定/文字列判定/配列判定/オブジェクト判定/真偽判定於x` |

See `apidoc_zh.md` for full signatures and examples.

---

## 7. References

- `apidoc_zh.md` — standard library full reference
- `ebnf_zh.md` — formal grammar in extended BNF
- `guide_zh.md` — tutorial guide with annotated examples
- `pyguide_zh.md` — guide for Python programmers
