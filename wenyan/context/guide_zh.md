# Wenyan Programming Guide

Wenyan (文言) is a Classical Chinese dialect of the Yui programming language.
Programs read like Classical Chinese prose: all operators and keywords are
replaced by Chinese phrases, strings are delimited by 「 」 brackets,
and comments begin with 注.

---

## 1. First Program

A bare expression statement evaluates and prints its result.

```wenyan
注 Print a greeting
「Hello, world!」
```

`吿曰EXPR。` is the explicit print statement.
Lines beginning with `注` (optionally `注、` or `注。`) are comments.

---

## 2. Variables, Increment, and Decrement

`吾有一數、曰VALUE、名之曰NAME。` assigns a value to a name.
**Value is written before name** — the reverse of most languages.

```wenyan
吾有一數、曰1、名之曰甲。
吾有一數、曰-2、名之曰乙。

增甲以一。
減乙以一。

>>> 甲
2
>>> 乙
-3
```

`>>> EXPR` followed by an expected literal is a **doctest** —
it asserts the expression equals the literal (Python doctest convention).

---

## 3. Types and Literals

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

- **Strings** are stored internally as **character-code arrays**, so all array
  operations (indexing, length, append) work on strings too.
- **Integers** are stored as **bit arrays (LSB first)**: `取6之第0` → `0`,
  `取6之第1` → `1`, `6之量` → `3`.

---

## 4. String Interpolation

Embed any expression inside a string with `{expr}`.

```wenyan
吾有一數、曰「Alice」、名之曰名。
吾有一數、曰12、名之曰齡。
吾有一數、曰「こんにちは、{名}さん！あなたは{齡}歳です。」、名之曰訊。

>>> 訊
「こんにちは、Aliceさん！あなたは12歳です。」
```

Escape `{` as `\{`. `\\`, `\n`, `\t` are also supported.

---

## 5. Arrays

`[...]` creates an array. `納EXPR入ARRAY。` appends an element to the end.

```wenyan
引標準庫
吾有一數、曰[1,2,3]、名之曰甲。

注 Append 0 to 甲
納0入甲。

注 Increment 甲[0]
增取甲之第0以一。

注 If 2 is in 甲, set 甲[0] = 甲[3]
若2含甲乎、則
   吾有一數、曰取甲之第3、名之曰取甲之第0。
條畢。

>>> 甲之量
4
```

### 5.1 Indexing and Length

- `取A之第i` — reads element at index `i` (0-based)
- `A之量` — number of elements

```wenyan
引標準庫
吾有一數、曰[10,20,30]、名之曰甲。
吾有一數、曰甲之量、名之曰n。

吾有一數、曰取甲之第0、名之曰首。
吾有一數、曰施差於n與1、名之曰末位。
吾有一數、曰取甲之第末位、名之曰末。

>>> 首
10
>>> 末
30

注 Write to index
吾有一數、曰200、名之曰取甲之第1。
>>> 取甲之第1
200
```

---

## 6. Objects

`{"key": value, ...}` creates an object. Keys are strings.
Object and array indexing both use `取CONTAINER之第KEY`.

```wenyan
吾有一數、曰{"x": 0, "y": 0}、名之曰O。
吾有一數、曰1、名之曰取O之第「x」。
吾有一數、曰2、名之曰取O之第「y」。

>>> 取O之第「x」
1
>>> 取O之第「y」
2
```

---

## 7. Strings Are Arrays

Strings are character-code arrays, so indexing and append work on strings too.

```wenyan
引標準庫
吾有一數、曰「hello」、名之曰s。

注 Overwrite first character with 'H'
吾有一數、曰取「H」之第0、名之曰取s之第0。

注 Append " world" character by character
吾有一數、曰「 world」、名之曰t。
吾有一數、曰0、名之曰i。
t之量度、
   納取t之第i入s。
   增i以一。
度畢。

>>> s
「Hello world」
```

---

## 7.5 Integers Are Bit Arrays

Integers are stored as bit arrays with the LSB first.

```wenyan
注 6 in binary is 110 → stored as [0, 1, 1] (LSB first)
>>> 取6之第0
0
>>> 取6之第1
1
>>> 取6之第2
1
>>> 6之量
3
```

A bit array and its integer compare equal:

```wenyan
>>> [0,1,1]等於6
然
```

### Bit AND Example

```wenyan
引標準庫
術曰位與以甲與乙
   吾有一數、曰甲之量、名之曰n。
   若乙之量小於n乎、則
      吾有一數、曰乙之量、名之曰n。
   條畢。
   吾有一數、曰0、名之曰i。
   吾有一數、曰[]、名之曰X。
   n度、
      吾有一數、曰0、名之曰x。
      若取甲之第i等於1乎、則
         若取乙之第i等於1乎、則
            吾有一數、曰1、名之曰x。
         條畢。
      條畢。
      納x入X。
      增i以一。
   度畢。
   以X答。
術畢。

>>> 施位與於6與5
4
>>> 施位與於3與1
1
```

---

## 8. Conditionals

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

```wenyan
吾有一數、曰然、名之曰旗。
吾有一數、曰0、名之曰果。
若旗等於然乎、則
   吾有一數、曰1、名之曰果。
否則
   吾有一數、曰2、名之曰果。
條畢。

>>> 果
1
```

### 8.1 Comparison Keywords

| Keyword | Operator | Example |
|---------|----------|---------|
| `等於` | `==` | `若x等於0乎、則` |
| `異於` | `!=` | `若x異於0乎、則` |
| `小於` | `<` | `若r小於b乎、則` |
| `大於` | `>` | `若x大於10乎、則` |
| `不大於` | `<=` | `若i不大於n乎、則` |
| `不小於` | `>=` | `若n不小於100乎、則` |
| `含` | `in` | `若「banana」含果乎、則` |
| `不含` | `not in` | `若「grape」不含果乎、則` |

```wenyan
吾有一數、曰[「apple」,「banana」,「cherry」]、名之曰果。
吾有一數、曰0、名之曰見。
吾有一數、曰0、名之曰無見。
若「banana」含果乎、則
   增見以一。
條畢。
若「grape」不含果乎、則
   增無見以一。
條畢。

>>> 見
1
>>> 無見
1
```

### 8.2 Multi-Branch (elif)

```wenyan
若x小於0乎、則
   吾有一數、曰-1、名之曰符。
否則
   若x大於0乎、則
      吾有一數、曰1、名之曰符。
   否則
      吾有一數、曰0、名之曰符。
   條畢。
條畢。
```

---

## 9. Loops

`N度、 ... 度畢。` executes a block N times. Exit early with `止。`.

```wenyan
吾有一數、曰0、名之曰計。
10度、
   增計以一。
   若計等於5乎、則
      止。
   條畢。
度畢。

>>> 計
5
```

To iterate over an array, manage an index variable manually:

```wenyan
引標準庫
吾有一數、曰[10,20,30]、名之曰甲。
吾有一數、曰0、名之曰i。
甲之量度、
   吿曰取甲之第i。
   增i以一。
度畢。
```

---

## 10. Functions

### 10.1 Definition and Return

```
術曰NAME以PARAM1與PARAM2…
   …
   以EXPR答。
術畢。
```

`以EXPR答。` returns a value. `還無。` returns without a value.
Local variables are invisible outside the function.

```wenyan
術曰後繼以n
   增n以一。
   以n答。
術畢。

>>> 施後繼於0
1
```

### 10.2 Zero-Argument Functions

Use `術曰NAME。` (with `。`) for functions that take no arguments.
Call with `施NAME以虛`.

```wenyan
術曰招呼。
   以「你好！」答。
術畢。

>>> 施招呼以虛
「你好！」
```

### 10.3 Implicit Return (Constructor Pattern)

If the body ends without `以...答。` or `還無。`, the runtime returns an object
containing all local variables.

```wenyan
術曰點以x與y
   注 no explicit return → returns {"x": x, "y": y}
術畢。
吾有一數、曰施點於3與5、名之曰O。

>>> 取O之第「x」
3
```

### 10.4 Multiple Return Values

**Using an array:**

```wenyan
引標準庫
術曰割以甲與乙
   吾有一數、曰施商於甲與乙、名之曰q。
   吾有一數、曰施剰余於甲與乙、名之曰r。
   以[q,r]答。
術畢。

>>> 施割於17與5
[3,2]
```

**Using an object:**

```wenyan
引標準庫
術曰統計以arr
   吾有一數、曰取arr之第0、名之曰lo。
   吾有一數、曰取arr之第0、名之曰hi。
   吾有一數、曰0、名之曰合計。
   吾有一數、曰arr之量、名之曰n。
   吾有一數、曰0、名之曰i。
   n度、
      吾有一數、曰取arr之第i、名之曰x。
      若x小於lo乎、則
         吾有一數、曰x、名之曰lo。
      條畢。
      若x大於hi乎、則
         吾有一數、曰x、名之曰hi。
      條畢。
      吾有一數、曰施和於合計與x、名之曰合計。
      增i以一。
   度畢。
   以{"min":lo,"max":hi,"sum":合計,"count":n}答。
術畢。
```

### 10.5 Recursion

```wenyan
引標準庫

術曰階乗以n
   若n等於0乎、則
      以1答。
   條畢。
   以施積於n與(施階乗於(施差於n與1))答。
術畢。

>>> 施階乗於0
1
>>> 施階乗於5
120
```

---

## 11. Standard Library

Declare `引標準庫` at the top. All functions use `施func於args` call syntax.

### 11.1 Arithmetic

| Function | Meaning |
|----------|---------|
| `施和於甲與乙與…` | Sum (array argument also accepted) |
| `施差於甲與乙` | Difference |
| `施積於甲與乙與…` | Product |
| `施商於甲與乙` | Quotient (floor division for integers) |
| `施剰余於甲與乙` | Remainder |

```wenyan
引標準庫

術曰最大公因以甲與乙
   甲度、
      若乙等於0乎、則
         止。
      條畢。
      吾有一數、曰施剰余於甲與乙、名之曰餘。
      吾有一數、曰乙、名之曰甲。
      吾有一數、曰餘、名之曰乙。
   度畢。
   以甲答。
術畢。

>>> 施最大公因於12與18
6
>>> 施最大公因於100與75
25
```

> **Integer division is floor division.** For a float result, convert first:
> `施商於(施小数化於甲)與(施小数化於乙)`.

### 11.2 Math Functions

```wenyan
引標準庫

>>> 施絶対値於-7
7
>>> 施平方根於9
3.000000
>>> 施最大値於3與1與4與1與5
5
>>> 施最小値於[10,20,30]
10
```

### 11.3 Type Conversion

```wenyan
引標準庫

>>> 施整数化於「42」
42
>>> 施整数化於3.700000
3
>>> 施小数化於5
5.000000
>>> 施文字列化於42
「42」
>>> 施配列化於「Hi」
[72, 105]
```

### 11.4 Type Check

```wenyan
引標準庫

>>> 施整数判定於42
然
>>> 施文字列判定於「hello」
然
>>> 施整数判定於「42」
否
```

---

## 12. Common Pitfalls

### Value comes before name in assignment

`吾有一數、曰VALUE、名之曰NAME。` — value is written **before** the name.
This is the reverse of most languages.

```wenyan
吾有一數、曰42、名之曰甲。   注 甲 = 42  (NOT 名之曰甲、曰42)
```

### No `continue` — use inverted condition or skip flag

Wenyan has `止。` (break) but no continue equivalent.

**Option A — invert the condition:**
```wenyan
n度、
   吾有一數、曰取arr之第i、名之曰x。
   若x大於0乎、則
      注 body here — only runs when x > 0
   條畢。
   增i以一。
度畢。
```

**Option B — skip flag:**
```wenyan
n度、
   吾有一數、曰取arr之第i、名之曰x。
   吾有一數、曰否、名之曰跳。
   若x不小於0乎、則
      吾有一數、曰然、名之曰跳。
   條畢。
   若跳異於然乎、則
      注 body here
   條畢。
   增i以一。
度畢。
```

### No pop/remove — manage a logical size separately

Wenyan arrays support `納x入arr。` (append) but not removal. When you need a
resizable stack, track a logical size variable:

```wenyan
吾有一數、曰[]、名之曰堆。
吾有一數、曰0、名之曰頂。

術曰推入以x
   若頂不小於堆之量乎、則
      納x入堆。
   否則
      吾有一數、曰x、名之曰取堆之第頂。
   條畢。
   增頂以一。
術畢。
```

### Integer division is floor division

`施商於甲與乙` with integer arguments uses **floor division**. For a float result,
convert at least one operand first:

```wenyan
引標準庫
>>> 施商於10與3
3
```

```wenyan
引標準庫
注 Float result:
施商於(施小数化於10)與(施小数化於3)   注 → 3.333333
```

---

## 13. Full Example: FizzBuzz

Counter-based approach — no remainder calls needed.

```wenyan
吾有一數、曰[]、名之曰果。
吾有一數、曰0、名之曰i。
吾有一數、曰0、名之曰三。
吾有一數、曰0、名之曰五。

100度、
   增i以一。
   增三以一。
   增五以一。
   若三等於3乎、則
      吾有一數、曰0、名之曰三。
   條畢。
   若五等於5乎、則
      吾有一數、曰0、名之曰五。
   條畢。
   若三等於0乎、則
      若五等於0乎、則
         納「FizzBuzz」入果。
      否則
         納「Fizz」入果。
      條畢。
   否則
      若五等於0乎、則
         納「Buzz」入果。
      否則
         納i入果。
      條畢。
   條畢。
度畢。

>>> 果之量
100
>>> 取果之第2
「Fizz」
>>> 取果之第4
「Buzz」
>>> 取果之第14
「FizzBuzz」
```

---

## 14. Full Example: Monte Carlo π Estimate

```wenyan
引標準庫

術曰蒙特卡羅以n
   吾有一數、曰0、名之曰中。
   n度、
      吾有一數、曰施乱数以虛、名之曰x。
      吾有一數、曰施乱数以虛、名之曰y。
      吾有一數、曰施平方根於(施和於(施積於x與x)與(施積於y與y))、名之曰距。
      若距不大於1乎、則
         增中以一。
      條畢。
   度畢。
   以施商於(施積於(施小数化於中)與4)與(施小数化於n)答。
術畢。

施蒙特卡羅於1000
```

`距不大於1` means `dist <= 1` — "not greater than 1".

---

## 15. Summary

- **Assignment**: `吾有一數、曰VALUE、名之曰NAME。` (value before name)
- **Index read**: `取ARRAY之第INDEX`
- **Index write**: `吾有一數、曰VALUE、名之曰取ARRAY之第INDEX。`
- **Append**: `納EXPR入ARRAY。`
- **Length**: `EXPR之量`
- **Condition**: `若COND乎、則 … 條畢。`; `否則` for else
- **Comparison**: `等於`/`異於`/`小於`/`大於`/`不大於`(≤)/`不小於`(≥)/`含`/`不含`
- **Loop**: `N度、 … 度畢。`; `止。` to break
- **Function**: `術曰NAME以PARAMS … 以EXPR答。 術畢。`
- **Function (no args)**: `術曰NAME。 … 術畢。`; call with `施NAME以虛`
- **Function call**: `施FUNC於ARG1與ARG2`
- **Arithmetic**: `施和/差/積/商/剰余於` — no `+`, `-`, `*`, `/`, `%`
- **Doctest**: `>>> EXPR` then expected literal on the next line

For the full formal grammar see `ebnf_zh.md`, and for complete stdlib signatures
see `apidoc_zh.md`.
