# Yui Programming Guide

Yui is an educational programming language written in Japanese.
It reduces symbols and follows natural Japanese word order so programs
can be read and written by beginners.

---

## 1. First Program

Writing a bare expression prints its value.

```yui
# Print a greeting
"Hello, world!"
```

Lines beginning with `#` (or `＃`) are **comments** and are ignored.

---

## 2. Variables, Increment, and Decrement

`name = expr` binds a value to a name. Re-assigning overwrites the previous value.
Numeric variables support the shorthand increment/decrement syntax.

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

`>>> expr` followed by an expected literal on the next line is a **doctest** —
it asserts that the expression equals the literal (Python doctest convention).

---

## 3. Types and Literals

Every value belongs to one of seven types.

| Type | Literal |
|------|---------|
| Null | `値なし` |
| Boolean | `真` / `偽` |
| Integer | `42` |
| Float | `3.14` (displayed with 6 decimal places) |
| String | `"あ"`, `"x={x}"` |
| Array | `[1, 2, 3]` |
| Object | `{"x": 1, "y": 2}` |

Strings are stored internally as **character-code arrays**, so all array operations
(indexing, length, append) apply equally to strings.

---

## 4. String Interpolation

Embed any expression inside a string with `{expr}`.

```yui
name = "ゆい"
age  = 12
msg  = "こんにちは、{name}さん！あなたは{age}歳です。"
msg

>>> msg
"こんにちは、ゆいさん！あなたは12歳です。"
```

Escape `{` as `\{` and `"` as `\"`. `\\`, `\n`, `\t` are also supported.

---

## 5. Arrays

`[...]` creates an array. `aにxを追加する` appends an element to the end.

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

### 5.1 Indexing and Length

- `a[i]` — element at index `i` (0-based)
- `aの大きさ` — number of elements

```yui
標準ライブラリを使う
A = [10, 20, 30]
n = Aの大きさ

first = A[0]
last  = A[差(n,1)]

>>> first
10
>>> last
30

A[1] = 200
>>> A[1]
200
```

---

## 6. Objects

`{"key": value, ...}` creates an object. Keys are strings.

```yui
O = {"x": 0, "y": 0}
O["x"] = 1
O["y"] = 2

>>> O["x"]
1
>>> O["y"]
2
```

---

## 7. Strings Are Arrays

Strings are character-code arrays, so indexing and append work on strings too.

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

---

## 7.5 Integers Are Bit Arrays

Integers are stored as bit arrays with the LSB first.

```yui
# 6 in binary is 110 → stored as [0, 1, 1] (LSB first)
>>> 6[0]
0
>>> 6[1]
1
>>> 6[2]
1
>>> 6の大きさ
3
```

A bit array and its integer compare equal:

```yui
>>> [0,1,1]が6
真
```

### Example: Bitwise AND

```yui
bits_and = 入力A,Bに対し{
   n = Aの大きさ
   もしBの大きさがnより小さいならば{
      n = Bの大きさ
   }
   i = 0
   X = 0
   n回くり返す{
      x = 0
      もしA[i]が1ならば{
         もしB[i]が1ならば{
            x = 1
         }
      }
      Xにxを追加する
      iを増やす
   }
   Xが答え
}

>>> bits_and(6, 5)
4
>>> bits_and(3, 1)
1
```

### Example: Right Shift

```yui
bits_rshift = 入力bits,kに対し{
   X = 0
   i = k
   bitsの大きさ回くり返す{
      もしiがbitsの大きさ以上ならば{
         くり返しを抜ける
      }
      Xにbits[i]を追加する
      iを増やす
   }
   Xが答え
}

>>> bits_rshift(6, 1)
3
>>> bits_rshift(12, 2)
3
```

---

## 8. Conditionals

```
もしxがyならば {
   …
}
そうでなければ {
   …
}
```

`そうでなければ` is optional. For elif-style chains, nest `もし` inside `そうでなければ`.

```yui
flag   = 真
result = 0

もしflagが真ならば{
   result = 1
}
そうでなければ{
   result = 2
}

>>> result
1
```

### 8.1 Comparison Suffixes

`==`, `!=`, `<`, `>`, `<=`, `>=` symbols are **not used** in Yui.

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

```yui
fruits = ["apple", "banana", "cherry"]
found   = 0
missing = 0

もし"banana"がfruitsのいずれかならば{ foundを増やす }
もし"grape"がfruitsのいずれでもないならば{ missingを増やす }

>>> found
1
>>> missing
1
```

### 8.2 Multi-Branch (elif)

There is no `elif`. Nest `もし` inside `そうでなければ`.

---

## 9. Loops

`N回くり返す { ... }` executes a block N times. Exit early with `くり返しを抜ける`.

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

---

## 10. Functions

### 10.1 Definition and Return

```
f = 入力 a, b, ... に対し {
   …
   expr が答え
}
```

`expr が答え` returns a value. `関数から抜ける` returns without a value.
Variables defined inside a function are **local** and invisible outside.

```yui
succ = 入力nに対し{
   nを増やす
   nが答え
}

>>> succ(0)
1
```

### 10.2 Implicit Return (Constructor Pattern)

If the body ends without `が答え` or `関数から抜ける`, the runtime returns an object
containing all local variables.

```yui
point = 入力x,yに対し{
   # no explicit return → returns {"x": x, "y": y}
}
O = point(3, 5)

>>> O["x"]
3
```

### 10.3 Recursion

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

>>> fact(0)
1
>>> fact(5)
120
```

---

## 11. Standard Library

Declare `標準ライブラリを使う` at the top. `+`, `-`, `*`, `/`, `%` **operators are not used** — call functions instead.

### 11.1 Arithmetic

| Function | Meaning |
|----------|---------|
| `和(x, …)` | Sum (array argument also accepted) |
| `差(x, y, …)` | Difference |
| `積(x, y, …)` | Product |
| `商(x, y)` | Quotient (floor division for integers) |
| `剰余(x, y)` | Remainder |

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
>>> gcd(100, 75)
25
```

> **Integer division is floor division.** For a float result, convert at least
> one operand first: `商(小数化(a), 小数化(b))`.

### 11.2 Math Functions

| Function | Result |
|----------|--------|
| `絶対値(x)` | Absolute value |
| `平方根(x)` | Square root (always float) |
| `最大値(…)` | Maximum (array accepted) |
| `最小値(…)` | Minimum (array accepted) |
| `乱数()` | Random float in [0, 1) |

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

| Function | Result |
|----------|--------|
| `整数化(x)` | Integer |
| `小数化(x)` | Float |
| `文字列化(x)` | String |
| `配列化(x)` | Character-code array (string) or key array (object) |

```yui
標準ライブラリを使う

>>> 整数化("42")
42
>>> 整数化(3.7)
3
>>> 小数化(5)
5.000000
>>> 文字列化(42)
"42"
>>> 配列化("Hi")
[72, 105]
```

### 11.4 Type Check

| Function | Returns `真` when… |
|----------|--------------------|
| `ブール判定(x)` | x is boolean |
| `整数判定(x)` | x is integer |
| `小数判定(x)` | x is float |
| `文字列判定(x)` | x is string |
| `配列判定(x)` | x is array |
| `オブジェクト判定(x)` | x is object |

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

## 12. Common Pitfalls

### No `continue` — use inverted condition or skip flag

Yui has `くり返しを抜ける` (break) but no continue equivalent.

**Option A — invert the condition:**
```yui
n回くり返す{
   x = arr[i]
   もしxが0より大きいならば{
      # body here — only runs when x > 0
   }
   iを増やす
}
```

**Option B — skip flag:**
```yui
n回くり返す{
   x = arr[i]
   skip = 偽
   もしxが0以下ならば{ skip = 真 }
   もしskipが偽ならば{
      # body here
   }
   iを増やす
}
```

### No pop/remove — manage a logical size separately

Arrays support `aにxを追加する` (append) but not removal. When you need a resizable
stack, track a logical size variable:

```yui
stack = []
top   = 0

push = 入力xに対し{
   もしtopがstackの大きさ以上ならば{
      stackにxを追加する
   }
   そうでなければ{
      stack[top] = x
   }
   topを増やす
   関数から抜ける
}
```

### Integer division is floor division

`商(a, b)` with integer arguments uses floor division. For a float result,
convert at least one operand first:

```yui
標準ライブラリを使う
>>> 商(7, 2)
3
```

```yui
# Float result:
商(小数化(7), 小数化(2))   # → 3.500000
```

---

## 13. Full Example: FizzBuzz

Counter-based approach — no remainder calls needed.

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

## 14. Full Example: Monte Carlo π Estimate

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

## 15. Summary

- **Assignment**: `x = expr`
- **Index**: `a[i]` (0-based); `aの大きさ` for length
- **Append**: `aにxを追加する`
- **Condition**: `もし A が B <suffix> ならば { … } そうでなければ { … }`
- **Comparison**: (none)=`==` / `以外`=`!=` / `より小さい`=`<` / `より大きい`=`>` / `以下`=`<=` / `以上`=`>=`
- **Loop**: `N回くり返す { … }`; `くり返しを抜ける` to break
- **Function**: `NAME = 入力PARAMS に対し { … expr が答え }`
- **Arithmetic**: `和`, `差`, `積`, `商`, `剰余` — no `+`, `-`, `*`, `/`, `%`
- **Doctest**: `>>> expr` then expected literal on the next line

For the full formal grammar see `ebnf_en.md`, and for complete stdlib signatures
see `apidoc_en.md`.
