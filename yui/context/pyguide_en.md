# Yui Programming Guide (for Python Users)

Yui is an educational programming language written in Japanese.
This guide introduces each feature by **first showing Python, then the equivalent
Yui code**, so Python programmers can learn Yui quickly.
Both constructs that exist in Python and those that don't are covered explicitly.

---

## 1. First Program

Python's `print` has a direct counterpart: in Yui, a standalone expression
evaluates and prints its result automatically.

**Python**

```python
print("Hello, world!")
```

**Yui**

```yui
# Print a greeting
"Hello, world!"
```

- In Yui, a **standalone expression** (not an assignment or control statement) is printed automatically (REPL-like behavior).
- Lines beginning with `#` (or `＃`) are comments.

---

## 2. Variables, Increment, and Decrement

**Python**

```python
x = 1
y = -2
x += 1
y -= 1
assert x == 2
assert y == -3
```

**Yui**

```yui
x = 1
y = -2
xを増やす
yを減らす

>>> x
2
>>> y
-3
```

- Yui's `>>> expr` + expected literal is the **same doctest convention as Python's `doctest` module** — inline tests embedded in source.
- `xを増やす` is `x += 1`; `yを減らす` is `y -= 1`.

---

## 3. Types and Literals

| Python | Yui | Yui literal |
|--------|-----|-------------|
| `None` | Null | `値なし` |
| `bool` | Boolean | `真` / `偽` |
| `int` | Integer | `42` |
| `float` | Float | `3.14` (displayed with 6 decimal places) |
| `str` | String | `"あ"` |
| `list` | Array | `[1, 2, 3]` |
| `dict` | Object | `{"x": 1, "y": 2}` |

Notes:
- Yui **strings are stored internally as character-code (int) arrays**. They support the same operations as `list` (append, length, indexing).
- Floats always display with 6 decimal places (`3.000000`).

---

## 4. String Interpolation

**Python** (f-string)

```python
name = "ゆい"
age = 12
msg = f"こんにちは、{name}さん！あなたは{age}歳です。"
assert msg == "こんにちは、ゆいさん！あなたは12歳です。"
```

**Yui**

```yui
name = "ゆい"
age  = 12
msg  = "こんにちは、{name}さん！あなたは{age}歳です。"

>>> msg
"こんにちは、ゆいさん！あなたは12歳です。"
```

- No `f` prefix needed. **Write `{expr}` directly inside any string**.
- Escape `{` as `\{` and `"` as `\"`. `\\`, `\n`, `\t` are also supported.

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

**Yui**

```yui
A = [1, 2, 3]
Aに0を追加する
A[0]を増やす
もし2がAのいずれかならば{
   A[0] = A[3]
}

>>> Aの大きさ
4
```

| Python | Yui |
|--------|-----|
| `A.append(x)` | `Aにxを追加する` |
| `len(A)` | `Aの大きさ` |
| `A[i]` | `A[i]` (same) |
| `x in A` | `もしxがAのいずれかならば` |
| `x not in A` | `もしxがAのいずれでもないならば` |

### 5.1 Indexing and Length

**Python**

```python
A = [10, 20, 30]
n = len(A)
first = A[0]
last = A[n - 1]
A[1] = 200
```

**Yui**

```yui
標準ライブラリを使う
A = [10, 20, 30]
n = Aの大きさ
first = A[0]
last  = A[差(n,1)]
A[1] = 200
```

- There is no `-` infix operator, so `n - 1` is written `差(n, 1)`.

---

## 6. Objects (Dicts)

**Python**

```python
O = {"x": 0, "y": 0}
O["x"] = 1
O["y"] = 2
assert O["x"] == 1
```

**Yui**

```yui
O = {"x": 0, "y": 0}
O["x"] = 1
O["y"] = 2

>>> O["x"]
1
```

Syntax is nearly identical to Python `dict`. Keys are strings.

---

## 7. Strings Are Arrays

In Python `str` and `list` are distinct. In Yui, strings **are** character-code arrays.

**Python**

```python
s = list("hello")
s[0] = ord("H")
for c in " world":
    s.append(ord(c))
```

**Yui**

```yui
s = "hello"
s[0] = "H"[0]

t = " world"
i = 0
tの大きさ回くり返す{
   sにt[i]を追加する
   iを増やす
}

>>> s
"Hello world"
```

- `"H"[0]` is the character code of `'H'`, same type as array elements.

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

**Yui**

```yui
flag   = 真
result = 0
もしflagが真ならば{
   result = 1
}
そうでなければ{
   result = 2
}
```

### 8.1 Comparison Operators → Suffixes

Yui does **not use** `==`, `!=`, `<`, `>`, `<=`, `>=` symbols. Write `もし A が B <suffix> ならば`.

| Python | Yui |
|--------|-----|
| `a == b` | `もしaがbならば` |
| `a != b` | `もしaがb以外ならば` |
| `a < b` | `もしaがbより小さいならば` |
| `a > b` | `もしaがbより大きいならば` |
| `a <= b` | `もしaがb以下ならば` |
| `a >= b` | `もしaがb以上ならば` |
| `a in xs` | `もしaがxsのいずれかならば` |
| `a not in xs` | `もしaがxsのいずれでもないならば` |

**Python**

```python
fruits = ["apple", "banana", "cherry"]
found = 1 if "banana" in fruits else 0
missing = 1 if "grape" not in fruits else 0
```

**Yui**

```yui
fruits = ["apple", "banana", "cherry"]
found   = 0
missing = 0
もし"banana"がfruitsのいずれかならば{ foundを増やす }
もし"grape"がfruitsのいずれでもないならば{ missingを増やす }
```

### 8.2 Multi-Branch (elif)

There is no `elif` in Yui. Nest `もし` inside `そうでなければ`.

---

## 9. Loops

Yui has only **count-based `N回くり返す`**. There is no `while` or `for x in xs`.

**Python**

```python
count = 0
for _ in range(10):
    count += 1
    if count == 5:
        break
assert count == 5
```

**Yui**

```yui
count = 0
10回くり返す{
   countを増やす
   もしcountが5ならば{
      くり返しを抜ける
   }
}

>>> count
5
```

| Python | Yui |
|--------|-----|
| `for _ in range(N):` | `N回くり返す{ … }` |
| `break` | `くり返しを抜ける` |

To iterate over an array, manage an index variable manually (see §7 String example).

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

**Yui**

```yui
succ = 入力nに対し{
   nを増やす
   nが答え
}

>>> succ(0)
1
```

| Python | Yui |
|--------|-----|
| `def f(a, b):` | `f = 入力 a, b に対し { … }` |
| `def f():` | `f = 入力なしに対し { … }` |
| `return x` | `x が答え` |
| `return` (no value) | `関数から抜ける` |

Variables defined inside a function are **local** (same as Python).

### 10.2 Implicit Return (Constructor Pattern)

In Python, a function without `return` returns `None`. In Yui, it returns an **object of all local variables**.

**Python equivalent**

```python
def point(x, y):
    return {"x": x, "y": y}

O = point(3, 5)
assert O["x"] == 3
```

**Yui**

```yui
point = 入力x,yに対し{
   # no explicit return → returns {"x": x, "y": y}
}
O = point(3, 5)

>>> O["x"]
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

**Yui**

```yui
標準ライブラリを使う

fact = 入力nに対し{
   もしnが0ならば{
      1が答え
   }
   そうでなければ{
      積(n, fact(差(n,1)))が答え
   }
}

>>> fact(5)
120
```

No `*` or `-` infix operators — use `積` and `差`.

---

## 11. Standard Library

Python has rich built-in operators, but Yui **performs arithmetic via functions**.
Declare `標準ライブラリを使う` before calling any library function.

### 11.1 Arithmetic

| Python | Yui |
|--------|-----|
| `a + b + c` | `和(a, b, c)` (array also: `和([a,b,c])`) |
| `a - b` | `差(a, b)` |
| `a * b` | `積(a, b)` |
| `a // b` | `商(a, b)` (floor division for int/int) |
| `a % b` | `剰余(a, b)` |

**Python**

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

assert gcd(12, 18) == 6
```

**Yui**

```yui
標準ライブラリを使う

gcd = 入力a,bに対し{
   a回くり返す{
      もしbが0ならば{
         くり返しを抜ける
      }
      r = 剰余(a, b)
      a = b
      b = r
   }
   aが答え
}

>>> gcd(12, 18)
6
```

Yui has no `while`, so simulate it with a **large repeat count + break**.

### 11.2 Math Functions

| Python | Yui |
|--------|-----|
| `abs(x)` | `絶対値(x)` |
| `math.sqrt(x)` | `平方根(x)` |
| `max(a, b, …)` / `max(xs)` | `最大値(a, b, …)` / `最大値(xs)` |
| `min(a, b, …)` / `min(xs)` | `最小値(a, b, …)` / `最小値(xs)` |
| `random.random()` | `乱数()` |

```yui
標準ライブラリを使う

>>> 絶対値(-7)
7
>>> 平方根(9)
3.000000
>>> 最大値(3, 1, 4, 1, 5)
5
>>> 最小値([10, 20, 30])
10
```

### 11.3 Type Conversion

| Python | Yui |
|--------|-----|
| `int(x)` | `整数化(x)` |
| `float(x)` | `小数化(x)` |
| `str(x)` | `文字列化(x)` |
| `list(s.encode())` (str→char-code list) | `配列化(x)` |

```yui
標準ライブラリを使う

>>> 整数化("42")
42
>>> 整数化(3.7)
3
>>> 文字列化(42)
"42"
>>> 配列化("Hi")
[72, 105]
```

### 11.4 Type Check

| Python | Yui |
|--------|-----|
| `isinstance(x, bool)` | `ブール判定(x)` |
| `isinstance(x, int)` | `整数判定(x)` |
| `isinstance(x, float)` | `小数判定(x)` |
| `isinstance(x, str)` | `文字列判定(x)` |
| `isinstance(x, list)` | `配列判定(x)` |
| `isinstance(x, dict)` | `オブジェクト判定(x)` |

```yui
標準ライブラリを使う

>>> 整数判定(42)
真
>>> 文字列判定("hello")
真
>>> 整数判定("42")
偽
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

**Yui** — counter-based approach, no remainder needed.

```yui
result = []
i    = 0
fizz = 0
buzz = 0

100回くり返す{
   iを増やす
   fizzを増やす
   buzzを増やす
   もしfizzが3ならば{ fizz = 0 }
   もしbuzzが5ならば{ buzz = 0 }

   もしfizzが0ならば{
      もしbuzzが0ならば{
         resultに"FizzBuzz"を追加する
      }そうでなければ{
         resultに"Fizz"を追加する
      }
   }そうでなければ{
      もしbuzzが0ならば{
         resultに"Buzz"を追加する
      }そうでなければ{
         resultにiを追加する
      }
   }
}

>>> resultの大きさ
100
>>> result[2]
"Fizz"
>>> result[4]
"Buzz"
>>> result[14]
"FizzBuzz"
```

---

## 13. Full Example: Monte Carlo π Estimate

**Python**

```python
import random, math

def monte_carlo(n):
    hits = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if math.sqrt(x*x + y*y) <= 1:
            hits += 1
    return 4 * hits / n

monte_carlo(1000)
```

**Yui**

```yui
標準ライブラリを使う

monte_carlo = 入力nに対し{
   hits = 0
   n回くり返す{
      x = 乱数()
      y = 乱数()
      dist = 平方根(和(積(x,x), 積(y,y)))
      もしdistが1以下ならば{
         hitsを増やす
      }
   }
   商(積(小数化(hits), 4), 小数化(n))が答え
}

monte_carlo(1000)
```

---

## 14. What Python Has That Yui Does Not

| Python feature | Yui equivalent / workaround |
|----------------|-----------------------------|
| `+`, `-`, `*`, `/`, `%` operators | `和/差/積/商/剰余` stdlib functions |
| `==`, `!=`, `<`, `>`, `<=`, `>=` | suffix keywords in `もし…ならば` |
| `while cond:` | `N回くり返す { } + くり返しを抜ける` |
| `for x in xs:` | Count loop with manual index variable |
| `elif` | Nested `もし` inside `そうでなければ` |
| `continue` | Inverted condition or skip-flag variable |
| `return` (no value) | `関数から抜ける` |
| No `return` → `None` | No explicit return → **object of all local vars** |
| `arr.pop()` / `del arr[i]` | Not available — manage a logical-size variable |
| Classes, exceptions, modules | Not available — Yui is intentionally minimal |

---

## 15. Summary

Yui's key differences from Python:

- **Japanese keywords** for all control flow; no arithmetic symbols.
- Comparisons use suffix `もし A が B <suffix> ならば`.
- Arithmetic uses `和`, `差`, `積`, `商`, `剰余` via function calls.
- Strings are character-code arrays and share operations with arrays.
- Functions: `NAME = 入力PARAMS に対し { … expr が答え }`.
- No explicit return → local variables returned as an object.
- Inline tests: `>>> expr` followed by expected value (Python doctest compatible).

| Concept | Python | Yui |
|---------|--------|-----|
| Assign | `x = 1` | `x = 1` |
| Read index | `arr[i]` | `arr[i]` |
| Write index | `arr[i] = v` | `arr[i] = v` |
| Append | `arr.append(x)` | `arrにxを追加する` |
| Length | `len(arr)` | `arrの大きさ` |
| If | `if cond:` | `もし cond ならば {` |
| Else | `else:` | `そうでなければ {` |
| For N | `for _ in range(N):` | `N回くり返す {` |
| Break | `break` | `くり返しを抜ける` |
| Def | `def f(a, b):` | `f = 入力 a, b に対し {` |
| Def (no args) | `def f():` | `f = 入力なしに対し {` |
| Return | `return x` | `x が答え` |
| Call | `f(a, b)` | `f(a, b)` |
| Add | `a + b` | `和(a, b)` |
| Multiply | `a * b` | `積(a, b)` |

For the formal grammar see `ebnf_en.md`, complete stdlib signatures see
`apidoc_en.md`, and quick syntax reference see `spec_en.md`.
