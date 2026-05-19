# Wenyan Programming Guide (for Python Users)

Wenyan is a Classical Chinese dialect of the Yui programming language.
This guide introduces each feature by **first showing Python, then the equivalent wenyan code**, so Python programmers can learn wenyan as quickly as possible.
Both constructs that exist in Python and those that don't are covered explicitly.

---

## 1. First Program

**Python**

```python
print("Hello, world!")
```

**Wenyan**

```wenyan
吿曰「Hello, world!」。
```

Or simply as a standalone expression:

```wenyan
「Hello, world!」
```

- Lines beginning with `注` are comments.
- `吿曰<expr>。` is the explicit print statement.
- A standalone expression statement evaluates and prints its value automatically.

---

## 2. Variables and Increment/Decrement

**Python**

```python
x = 1
y = -2
x += 1
y -= 1
assert x == 2
assert y == -3
```

**Wenyan**

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

- `吾有一數、曰<value>、名之曰<name>。` assigns a value (**value comes before name** — reversed from Python's `name = value`).
- `增x以一。` is equivalent to `x += 1`; `減x以一。` is equivalent to `x -= 1`.
- `>>> <expr>` followed by an expected value is an inline test (Python doctest compatible).

---

## 3. Types and Literals

| Python | Wenyan  | Wenyan literal       |
|--------|---------|----------------------|
| `None` | null    | `無`                 |
| `bool` | boolean | `然` / `否`          |
| `int`  | integer | `42`                 |
| `float`| decimal | `3.14` (displayed with 6 decimal places) |
| `str`  | string  | `「hello」`          |
| `list` | array   | `[1, 2, 3]`          |
| `dict` | object  | `{"x": 1, "y": 2}`   |

Notes:
- Wenyan **strings are internally stored as arrays of character codes** (integers). They share the same operations (append, length) as arrays.
- Floats are always displayed with 6 decimal places: `3.000000`.

---

## 4. String Interpolation

**Python** (f-string)

```python
name = "Alice"
age = 12
msg = f"Hello, {name}! You are {age} years old."
```

**Wenyan**

```wenyan
吾有一數、曰「Alice」、名之曰名。
吾有一數、曰12、名之曰齡。
吾有一數、曰「Hello, {名}! You are {齡} years old.」、名之曰訊。

>>> 訊
「Hello, Alice! You are 12 years old.」
```

- No special prefix needed. **Any string literal can contain `{expr}` interpolations**.
- To include a literal `{`, use `\{`. `\\`, `\n`, `\t` also work.

---

## 5. Arrays (Lists)

**Python**

```python
A = [1, 2, 3]
A.append(0)
A[0] += 1
if 2 in A:
    A[0] = A[3]
assert len(A) == 4
```

**Wenyan**

```wenyan
引標準庫
吾有一數、曰[1,2,3]、名之曰甲。
納0入甲。
增取甲之第0以一。
若2含甲乎、則
   吾有一數、曰取甲之第3、名之曰取甲之第0。
條畢。

>>> 甲之量
4
```

Correspondence table:

| Python               | Wenyan                                     |
|----------------------|--------------------------------------------|
| `A.append(x)`        | `納x入A。`                                 |
| `len(A)`             | `A之量`                                    |
| `A[i]`               | `取A之第i`                                 |
| `A[i] = v`           | `吾有一數、曰v、名之曰取A之第i。`           |
| `x in A`             | `若x含A乎、則`                             |
| `x not in A`         | `若x不含A乎、則`                           |

### 5.1 Indexing and Length

**Python**

```python
A = [10, 20, 30]
n = len(A)
first = A[0]
last = A[n - 1]
A[1] = 200
```

**Wenyan**

```wenyan
引標準庫
吾有一數、曰[10,20,30]、名之曰甲。
吾有一數、曰甲之量、名之曰n。
吾有一數、曰取甲之第0、名之曰首。
吾有一數、曰施差於n與1、名之曰末位。
吾有一數、曰取甲之第末位、名之曰末。
吾有一數、曰200、名之曰取甲之第1。
```

- Since `-` infix is not available, `n - 1` is written `施差於n與1`.

---

## 6. Objects (Dictionaries)

**Python**

```python
O = {"x": 0, "y": 0}
O["x"] = 1
O["y"] = 2
assert O["x"] == 1
```

**Wenyan**

```wenyan
吾有一數、曰{"x": 0, "y": 0}、名之曰O。
吾有一數、曰1、名之曰取O之第「x」。
吾有一數、曰2、名之曰取O之第「y」。

>>> 取O之第「x」
1
```

Both arrays and objects use `取<container>之第<key>` for indexing.

---

## 7. Strings Are Arrays

In Python, `str` and `list` are distinct types. In wenyan (and Yui), **a string is an array of character codes**.

**Python**

```python
s = list("hello")
s[0] = ord("H")
print("".join(chr(c) for c in s))  # "Hello"
```

**Wenyan**

```wenyan
引標準庫
吾有一數、曰「hello」、名之曰s。
吾有一數、曰取「H」之第0、名之曰取s之第0。

>>> s
「Hello」
```

- `取「H」之第0` gives the character code for `'H'` (72).
- Array elements and string characters are the same type (integer character codes).

---

## 8. Conditionals

**Python**

```python
flag = True
if flag:
    result = 1
else:
    result = 2
```

**Wenyan**

```wenyan
吾有一數、曰然、名之曰旗。
吾有一數、曰0、名之曰果。
若旗等於然乎、則
   吾有一數、曰1、名之曰果。
否則
   吾有一數、曰2、名之曰果。
條畢。
```

### 8.1 Comparison Operators

Wenyan does not use `==`, `!=`, `<`, `>` etc. as symbols inside `若`. Instead it uses Classical Chinese words.

| Python         | Wenyan                         |
|----------------|--------------------------------|
| `a == b`       | `若a等於b乎、則`               |
| `a != b`       | `若a異於b乎、則`               |
| `a < b`        | `若a小於b乎、則`               |
| `a <= b`       | `若a不大於b乎、則`             |
| `a > b`        | `若a大於b乎、則`               |
| `a >= b`       | `若a不小於b乎、則`             |
| `a in xs`      | `若a含xs乎、則`                |
| `a not in xs`  | `若a不含xs乎、則`              |

**Python**

```python
fruits = ["apple", "banana", "cherry"]
found = 1 if "banana" in fruits else 0
```

**Wenyan**

```wenyan
吾有一數、曰[「apple」,「banana」,「cherry」]、名之曰果。
吾有一數、曰0、名之曰見。
若「banana」含果乎、則
   吾有一數、曰1、名之曰見。
條畢。
```

### 8.2 Multi-Way Branching

Wenyan has no `elif`. Nest `若` inside `否則` to achieve the same effect.

**Python**

```python
if x < 0:
    sign = -1
elif x > 0:
    sign = 1
else:
    sign = 0
```

**Wenyan**

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

Wenyan's only loop construct is **`<N>度、 ... 度畢。`**. There is no `while` or `for x in xs`.

**Python**

```python
count = 0
for _ in range(10):
    count += 1
    if count == 5:
        break
assert count == 5
```

**Wenyan**

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

| Python                    | Wenyan             |
|---------------------------|--------------------|
| `for _ in range(N):`      | `N度、 ... 度畢。` |
| `break`                   | `止。`             |

To iterate over an array, use an index variable and increment it manually:

```wenyan
引標準庫
吾有一數、曰[10,20,30]、名之曰甲。
吾有一數、曰0、名之曰i。
甲之量度、
   吿曰取甲之第i。
   增i以一。
度畢。
```

Note: `甲之量度、` repeats `甲之量` (= the current length of `甲`) times.

---

## 10. Functions

### 10.1 Definition and Return

**Python**

```python
def succ(n):
    n += 1
    return n

assert succ(0) == 1
```

**Wenyan**

```wenyan
術曰後繼以n
   增n以一。
   以n答。
術畢。

>>> 施後繼於0
1
```

| Python              | Wenyan                                        |
|---------------------|-----------------------------------------------|
| `def f(a, b):`      | `術曰f以a與b`                                 |
| `def f():`          | `術曰f。`                                     |
| `return x`          | `以x答。`                                     |
| `return` (no value) | `還無。`                                      |
| `f(a, b)`           | `施f於a與b`                                   |
| `f()`               | `施f以虛`                                     |

Variables defined inside a function are **local** (same as Python).

### 10.2 Implicit Return Value (Constructor Style)

In Python, a function without `return` returns `None`. In wenyan, it returns **an object containing all local variables**.

**Python (equivalent)**

```python
def point(x, y):
    return {"x": x, "y": y}

O = point(3, 5)
assert O["x"] == 3
```

**Wenyan**

```wenyan
術曰點以x與y
   注 no return — local vars become a dict
術畢。
吾有一數、曰施點於3與5、名之曰O。

>>> 取O之第「x」
3
```

### 10.3 Recursion

**Python**

```python
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

assert fact(5) == 120
```

**Wenyan**

```wenyan
引標準庫

術曰階乘以n
   若n等於0乎、則
      以1答。
   條畢。
   以施積於n與(施階乘於(施差於n與1))答。
術畢。

>>> 施階乘於5
120
```

Since `*` and `-` infix operators are unavailable, use `積` and `差` from the standard library.

---

## 11. Standard Library

The standard library must be declared at the top of the program with `引標準庫`. All functions use wenyan's `施f於arg` call syntax.

### 11.1 Arithmetic

| Python         | Wenyan                                              |
|----------------|-----------------------------------------------------|
| `a + b`        | `施和於a與b` (also: `施和於[a, b, c]`)              |
| `a - b`        | `施差於a與b`                                        |
| `a * b`        | `施積於a與b` (also: `施積於[a, b, c]`)              |
| `a // b`       | `施商於a與b` (floor division for ints)              |
| `a % b`        | `施剰余於a與b` (alias: `施餘於a與b`)                |

**Python**

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

assert gcd(12, 18) == 6
```

**Wenyan**

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
```

Since wenyan has no `while`, simulate it with a large repeat count and `止。` (break).

### 11.2 Math Functions

| Python                       | Wenyan                                   |
|------------------------------|------------------------------------------|
| `abs(x)`                     | `施絶対値於x`                            |
| `math.sqrt(x)`               | `施平方根於x`                            |
| `max(a, b, ...)` / `max(xs)` | `施最大値於a與b` / `施最大値於xs`        |
| `min(a, b, ...)` / `min(xs)` | `施最小値於a與b` / `施最小値於xs`        |
| `random.random()`            | `施乱数以虛`                             |

**Wenyan**

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

| Python           | Wenyan               |
|------------------|----------------------|
| `int(x)`         | `施整数化於x`        |
| `float(x)`       | `施小数化於x`        |
| `str(x)`         | `施文字列化於x`      |
| `list(s)` (str → char-code list) | `施配列化於x` |

**Wenyan**

```wenyan
引標準庫

>>> 施整数化於「42」
42
>>> 施整数化於3.700000
3
>>> 施文字列化於42
「42」
>>> 施配列化於「Hi」
[72,105]
```

### 11.4 Type Predicates

| Python                      | Wenyan                  |
|-----------------------------|-------------------------|
| `isinstance(x, bool)`       | `施真偽判定於x`         |
| `isinstance(x, int)`        | `施整数判定於x`         |
| `isinstance(x, float)`      | `施小数判定於x`         |
| `isinstance(x, str)`        | `施文字列判定於x`       |
| `isinstance(x, list)`       | `施配列判定於x`         |
| `isinstance(x, dict)`       | `施オブジェクト判定於x` |

**Wenyan**

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

## 12. Full Example: FizzBuzz

**Python**

```python
result = []
for i in range(1, 101):
    if i % 15 == 0:
        result.append("FizzBuzz")
    elif i % 3 == 0:
        result.append("Fizz")
    elif i % 5 == 0:
        result.append("Buzz")
    else:
        result.append(i)
assert len(result) == 100
```

**Wenyan**

Using counters instead of modulo to determine Fizz/Buzz:

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

## 13. Full Example: GCD

**Python**

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

**Wenyan**

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

---

## 14. Things Python Has That Wenyan Doesn't

Common pitfalls for Python programmers:

- **No infix operators**: `+ - * / % == != < <= > >=` are all unavailable. Use `施和/差/積/商/剰余於...與...` for arithmetic; use `若A等於/異於/小於/大於/不大於/不小於B乎、則` for comparison.
- **No `while` or `for x in xs`**: Only `N度、 ... 度畢。` exists. Iterate arrays manually with an index variable.
- **No `elif`**: Nest `若` inside `否則` blocks.
- **No-argument functions use `術曰f。`**: Define with `術曰f。` and call with `施f以虛`.
- **Implicit object return**: A function body with no `以...答。` returns a dict of its local variables — not `None` as in Python.
- **Assignment is reversed**: `吾有一數、曰value、名之曰name。` — value comes first, then name.
- **No classes, exceptions, or operator overloading**: Wenyan (and Yui) is intentionally minimal.

---

## 15. Summary

Compared to Python, wenyan's key characteristics are:

- **Classical Chinese keywords**: variable assignment, loops, conditionals, and function definitions all use Classical Chinese phrases.
- Comparisons use `若A等於/異於/小於/大於/不大於/不小於B乎、則`.
- Arithmetic uses `和`, `差`, `積`, `商`, `剰余` from the standard library via `施func於args`.
- Strings are character-code arrays, unified with the array type; use `「...」` for string literals.
- Functions are defined with `術曰name以params ... 術畢。` and return with `以expr答。`.
- Function calls use `施func於arg1與arg2` syntax.
- Inline tests use `>>> expr` followed by the expected value (Python doctest compatible).

For the formal grammar, see `ebnf_wenyan.md`. For code examples, see `codesample_all_wenyan.md`.
