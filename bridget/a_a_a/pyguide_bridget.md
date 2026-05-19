# Bridget Programming Guide (for Python Users)

Bridget is a plain-English dialect of the Yui programming language.
This guide introduces each feature by **first showing Python, then the equivalent bridget code**, so Python programmers can learn bridget as quickly as possible.
Both constructs that exist in Python and those that don't are covered explicitly.

---

## 1. First Program

Python's `print` has an analogue in bridget: a standalone expression is automatically printed (REPL-style behaviour). There is also an explicit print statement.

**Python**

```python
print("Hello, world!")
```

**Bridget**

```bridget
Now, "Hello, world!"
```

Or simply as a standalone expression:

```bridget
"Hello, world!"
```

- Lines beginning with `#` are comments.
- `Now, <expr>` is the explicit print statement.
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

**Bridget**

```bridget
Remember that x is 1
Remember that y is -2
Increase x
Decrease y

>>> x
2
>>> y
-3
```

- `Remember that <var> is <expr>` assigns a value (equivalent to Python's `=`).
- `Increase x` is equivalent to `x += 1`; `Decrease y` is equivalent to `y -= 1`.
- `>>> <expr>` followed by an expected value is an inline test (Python doctest compatible).

---

## 3. Types and Literals

| Python | Bridget | Bridget literal |
|--------|---------|-----------------|
| `None` | null    | `nothing`       |
| `bool` | boolean | `yes` / `no`    |
| `int`  | integer | `42`            |
| `float`| decimal | `3.14` (displayed with 6 decimal places) |
| `str`  | string  | `"hello"`       |
| `list` | array   | `[1, 2, 3]`     |
| `dict` | object  | `{"x": 1, "y": 2}` |

Notes:
- Bridget **strings are internally stored as arrays of character codes** (integers). They share the same operations (append, length) as arrays.
- Floats are always displayed with 6 decimal places: `3.000000`.
- `yes`/`no` are only treated as boolean literals when not followed by an identifier character.

---

## 4. String Interpolation

**Python** (f-string)

```python
name = "Alice"
age = 12
msg = f"Hello, {name}! You are {age} years old."
assert msg == "Hello, Alice! You are 12 years old."
```

**Bridget**

```bridget
Remember that name is "Alice"
Remember that age is 12
Remember that msg is "Hello, {name}! You are {age} years old."

>>> msg
"Hello, Alice! You are 12 years old."
```

- No `f` prefix is needed. **Any string literal can contain `{expr}` interpolations**.
- To include a literal `{` or `"`, use `\{` or `\"`. `\\`, `\n`, `\t` also work.

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

**Bridget**

```bridget
Use the standard library
Remember that A is [1, 2, 3]
Add A to 0
Increase item 0 in A
When 2 is in A, then:
   Remember that item 0 in A is item 3 in A
End when

>>> A's length
4
```

Correspondence table:

| Python               | Bridget                             |
|----------------------|-------------------------------------|
| `A.append(x)`        | `Add A to x`                        |
| `len(A)`             | `A's length`                        |
| `A[i]`               | `item i in A`                       |
| `A[i] = v`           | `Remember that item i in A is v`    |
| `x in A`             | `When x is in A, then:`             |
| `x not in A`         | `When x is not in A, then:`         |

### 5.1 Indexing and Length

**Python**

```python
A = [10, 20, 30]
n = len(A)
first = A[0]
last = A[n - 1]
A[1] = 200
```

**Bridget**

```bridget
Use the standard library
Remember that A is [10, 20, 30]
Remember that n is A's length
Remember that first is item 0 in A
Remember that last is item (diff of n and 1) in A
Remember that item 1 in A is 200
```

- Since `-` infix is not available, `n - 1` is written `diff of n and 1`.

---

## 6. Objects (Dictionaries)

**Python**

```python
O = {"x": 0, "y": 0}
O["x"] = 1
O["y"] = 2
assert O["x"] == 1
```

**Bridget**

```bridget
Remember that O is {"x": 0, "y": 0}
Remember that item "x" in O is 1
Remember that item "y" in O is 2

>>> item "x" in O
1
```

The syntax mirrors array indexing — both arrays and objects use `item <key> in <container>`.

---

## 7. Strings Are Arrays

In Python, `str` and `list` are distinct types. In bridget (and Yui), **a string is an array of character codes**.

**Python**

```python
s = list("hello")
s[0] = ord("H")
for c in " world":
    s.append(ord(c))
print("".join(chr(c) for c in s))  # "Hello world"
```

**Bridget**

```bridget
Use the standard library
Remember that s is "hello"
Remember that item 0 in s is item 0 in "H"

Remember that t is " world"
Remember that i is 0
Do this t's length times:
   Add s to item i in t
   Increase i
End do

>>> s
"Hello world"
```

- `item 0 in "H"` gives the character code for `'H'` (72).
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

**Bridget**

```bridget
Remember that flag is yes
Remember that result is 0
When flag is yes, then:
   Remember that result is 1
But, if not:
   Remember that result is 2
End when
```

### 8.1 Comparison Operators

Bridget does not use `==`, `!=`, `<`, `>` etc. as symbols. Instead it uses phrases inside `When ... then:`.

| Python         | Bridget                              |
|----------------|--------------------------------------|
| `a == b`       | `When a is b, then:`                 |
| `a != b`       | `When a is not b, then:`             |
| `a < b`        | `When a is less than b, then:`       |
| `a <= b`       | `When a is at least b, then:`        |
| `a > b`        | `When a is more than b, then:`       |
| `a >= b`       | `When a is at most b, then:`         |
| `a in xs`      | `When a is in xs, then:`             |
| `a not in xs`  | `When a is not in xs, then:`         |

> **Warning:** `is at least` means `≤` and `is at most` means `≥`. These are reversed from standard English intuition.

**Python**

```python
fruits = ["apple", "banana", "cherry"]
found = 1 if "banana" in fruits else 0
missing = 1 if "grape" not in fruits else 0
```

**Bridget**

```bridget
Remember that fruits is ["apple", "banana", "cherry"]
Remember that found is 0
Remember that missing is 0
When "banana" is in fruits, then:
   Increase found
End when
When "grape" is not in fruits, then:
   Increase missing
End when
```

### 8.2 Multi-Way Branching

Bridget has no `elif`. Nest `When` inside `But, if not:` to achieve the same effect.

**Python**

```python
if x < 0:
    sign = -1
elif x > 0:
    sign = 1
else:
    sign = 0
```

**Bridget**

```bridget
When x is less than 0, then:
   Remember that sign is -1
But, if not:
   When x is more than 0, then:
      Remember that sign is 1
   But, if not:
      Remember that sign is 0
   End when
End when
```

---

## 9. Loops

Bridget's only loop construct is **`Do this N times:`**. There is no `while` or `for x in xs`.

**Python**

```python
count = 0
for _ in range(10):
    count += 1
    if count == 5:
        break
assert count == 5
```

**Bridget**

```bridget
Remember that count is 0
Do this 10 times:
   Increase count
   When count is 5, then:
      Leave the loop
   End when
End do

>>> count
5
```

| Python                    | Bridget                        |
|---------------------------|--------------------------------|
| `for _ in range(N):`      | `Do this N times:`             |
| `break`                   | `Leave the loop`               |

To iterate over an array, use an index variable and increment it manually:

```bridget
Use the standard library
Remember that A is [10, 20, 30]
Remember that i is 0
Do this A's length times:
   Now, item i in A
   Increase i
End do
```

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

**Bridget**

```bridget
This is how to succ of n:
   Increase n
   The answer is n
Now you know

>>> succ of 0
1
```

| Python              | Bridget                                     |
|---------------------|---------------------------------------------|
| `def f(a, b):`      | `This is how to f of a and b:`              |
| `def f():`          | `This is how to f ^^:`                      |
| `return x`          | `The answer is x`                           |
| `return` (no value) | `Stop here`                                 |
| `f(a, b)`           | `f of a and b`                              |
| `f()`               | `f, do it`                                  |

Variables defined inside a function are **local** (same as Python).

### 10.2 Implicit Return Value (Constructor Style)

In Python, a function without `return` returns `None`. In bridget, it returns **an object containing all local variables** — useful as a lightweight record constructor.

**Python (equivalent)**

```python
def point(x, y):
    return {"x": x, "y": y}

O = point(3, 5)
assert O["x"] == 3
```

**Bridget**

```bridget
This is how to point of x and y:
   # no return — local vars become a dict
Now you know
Remember that O is point of 3 and 5

>>> item "x" in O
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

**Bridget**

```bridget
Use the standard library

This is how to fact of n:
   When n is 0, then:
      The answer is 1
   End when
   The answer is product of n and (fact of (diff of n and 1))
Now you know

>>> fact of 5
120
```

Since `*` and `-` infix operators are unavailable, use `product` and `diff` from the standard library.

---

## 11. Standard Library

The standard library must be declared at the top of the program with `Use the standard library`. All functions use bridget's `f of arg` call syntax.

### 11.1 Arithmetic

| Python         | Bridget                                         |
|----------------|-------------------------------------------------|
| `a + b`        | `sum of a and b` (also: `sum of [a, b, c]`)     |
| `a - b`        | `diff of a and b`                               |
| `a * b`        | `product of a and b`                            |
| `a // b`       | `quotient of a and b` (floor division for ints) |
| `a % b`        | `remainder of a and b`                          |

**Python**

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

assert gcd(12, 18) == 6
```

**Bridget**

```bridget
Use the standard library

This is how to gcd of a and b:
   Do this a times:
      When b is 0, then:
         Leave the loop
      End when
      Remember that r is remainder of a and b
      Remember that a is b
      Remember that b is r
   End do
   The answer is a
Now you know

>>> gcd of 12 and 18
6
```

Since bridget has no `while`, simulate it with a large repeat count and `Leave the loop`.

### 11.2 Math Functions

| Python                       | Bridget                              |
|------------------------------|--------------------------------------|
| `abs(x)`                     | `abs of x`                           |
| `math.sqrt(x)`               | `sqrt of x`                          |
| `max(a, b, ...)` / `max(xs)` | `max of a and b` / `max of xs`       |
| `min(a, b, ...)` / `min(xs)` | `min of a and b` / `min of xs`       |
| `random.random()`            | `random, do it`                      |

**Bridget**

```bridget
Use the standard library

>>> abs of -7
7
>>> sqrt of 9
3.000000
>>> max of 3 and 1 and 4 and 1 and 5
5
>>> min of [10, 20, 30]
10
```

### 11.3 Type Conversion

| Python           | Bridget            |
|------------------|--------------------|
| `int(x)`         | `toint of x`       |
| `float(x)`       | `tofloat of x`     |
| `str(x)`         | `tostring of x`    |
| `list(s)` (str → char-code list) | `toarray of x` |

**Bridget**

```bridget
Use the standard library

>>> toint of "42"
42
>>> toint of 3.700000
3
>>> tostring of 42
"42"
>>> toarray of "Hi"
[72, 105]
```

### 11.4 Type Predicates

| Python                      | Bridget            |
|-----------------------------|--------------------|
| `isinstance(x, bool)`       | `isbool of x`      |
| `isinstance(x, int)`        | `isint of x`       |
| `isinstance(x, float)`      | `isfloat of x`     |
| `isinstance(x, str)`        | `isstring of x`    |
| `isinstance(x, list)`       | `isarray of x`     |
| `isinstance(x, dict)`       | `isobject of x`    |

**Bridget**

```bridget
Use the standard library

>>> isint of 42
yes
>>> isstring of "hello"
yes
>>> isint of "42"
no
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

**Bridget**

Using counters instead of modulo to determine Fizz/Buzz:

```bridget
Remember that result is []
Remember that i is 0
Remember that fizz is 0
Remember that buzz is 0

Do this 100 times:
   Increase i
   Increase fizz
   Increase buzz
   When fizz is 3, then:
      Remember that fizz is 0
   End when
   When buzz is 5, then:
      Remember that buzz is 0
   End when
   When fizz is 0, then:
      When buzz is 0, then:
         Add result to "FizzBuzz"
      But, if not:
         Add result to "Fizz"
      End when
   But, if not:
      When buzz is 0, then:
         Add result to "Buzz"
      But, if not:
         Add result to i
      End when
   End when
End do

>>> result's length
100
>>> item 2 in result
"Fizz"
>>> item 4 in result
"Buzz"
>>> item 14 in result
"FizzBuzz"
```

---

## 13. Full Example: Monte Carlo π Estimation

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

**Bridget**

```bridget
Use the standard library

This is how to monte_carlo of n:
   Remember that hits is 0
   Do this n times:
      Remember that x is random, do it
      Remember that y is random, do it
      Remember that dist is sqrt of (sum of (product of x and x) and (product of y and y))
      When dist is at least 1, then:
         Increase hits
      End when
   End do
   The answer is quotient of (product of (tofloat of hits) and 4) and (tofloat of n)
Now you know

monte_carlo of 1000
```

Note: `When dist is at least 1` means `dist ≤ 1` in bridget.

---

## 14. Things Python Has That Bridget Doesn't

Common pitfalls for Python programmers:

- **No infix operators**: `+ - * / % == != < <= > >=` are all unavailable. Use `sum`/`diff`/`product`/`quotient`/`remainder` for arithmetic; use `When A is ... B, then:` for comparison.
- **No `while` or `for x in xs`**: Only `Do this N times: ... End do` exists. Iterate arrays manually with an index variable.
- **No `elif`**: Nest `When` inside `But, if not:` blocks.
- **No-argument functions need `^^`**: Write `This is how to f ^^:` and call with `f, do it`.
- **Implicit object return**: A function body with no `The answer is` returns a dict of its local variables — not `None` as in Python.
- **No classes, exceptions, or operator overloading**: Bridget (and Yui) is intentionally minimal.
- **`is at least` means `≤`, `is at most` means `≥`**: Counter-intuitive but fixed by the language spec.

---

## 15. Summary

Compared to Python, bridget's key characteristics are:

- **No symbols — write in plain English**: comparisons and arithmetic use words, not operators.
- Comparisons use `When A is [less than / more than / at least / at most] B, then:`.
- Arithmetic uses `sum`, `diff`, `product`, `quotient`, `remainder` from the standard library.
- Strings are character-code arrays, unified with the array type.
- Functions are defined with `This is how to ... Now you know` and return with `The answer is`.
- Inline tests use `>>> expr` followed by the expected value (Python doctest compatible).

For the formal grammar, see `pro159/ebnf_bridget.md`. For code examples, see `pro159/codesample_all_bridget.md`.
