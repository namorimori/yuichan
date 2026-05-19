# Bridget Programming Guide (for Python Users)

Bridget is a plain-English programming language built on the Yui runtime.
This guide shows **each feature first in Python, then in Bridget**, so Python
programmers can pick up Bridget quickly by mapping familiar patterns to the
new syntax.

---

## 1. First Program

Python's `print` has a direct counterpart: in Bridget, a bare expression
statement evaluates and prints its result automatically.

**Python**

```python
print("Hello, world!")
```

**Bridget**

```bridget
# Print a greeting
"Hello, world!"
```

- Any standalone expression (not an assignment or control statement) is
  printed automatically — like a REPL.
- Lines beginning with `#` are comments.

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

- `Remember that NAME is EXPR` is the assignment statement — there is no `=`.
- `Increase x` is `x += 1`; `Decrease x` is `x -= 1`.
- `>>> EXPR` followed by an expected literal is a **doctest assert**, identical
  in convention to Python's `doctest` module.

---

## 3. Types and Literals

| Python | Bridget | Bridget literal |
|--------|---------|-----------------|
| `None` | Null | `Nothing` / `nothing` / `null` |
| `bool` | Boolean | `Yes` / `yes` / `true` · `No` / `no` / `false` |
| `int` | Integer | `42` |
| `float` | Float | `3.14` (displayed with 6 decimal places) |
| `str` | String | `"hello"` |
| `list` | Array | `[1, 2, 3]` |
| `dict` | Object | `{"x": 1, "y": 2}` |

Notes:

- Bridget **strings are stored internally as character-code (int) arrays**, so
  all array operations (indexing, length, append) work on strings too.
- Floats always display with 6 decimal places: `3.000000`.

---

## 4. String Interpolation

**Python** (f-string)

```python
name = "Bridget"
age = 3
msg = f"Hello, {name}! You are {age} years old."
assert msg == "Hello, Bridget! You are 3 years old."
```

**Bridget**

```bridget
Remember that name is "Bridget"
Remember that age is 3
Remember that msg is "Hello, {name}! You are {age} years old."

>>> msg
"Hello, Bridget! You are 3 years old."
```

- No `f` prefix needed. **Any string literal with `{expr}` is interpolated.**
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

**Bridget**

```bridget
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

| Python | Bridget |
|--------|---------|
| `A.append(x)` | `Add A to x` |
| `len(A)` | `A's length` |
| `A[i]` (read) | `item i in A` |
| `A[i] = v` (write) | `Remember that item i in A is v` |
| `x in A` | `x is in A` |
| `x not in A` | `x is not in A` |

> **Watch out — `Add A to x` is array first, element second.**
> This is the reverse of the natural English "add X to Y":
> `Add A to 0` means "append 0 to A", not "append A to 0".

### 5.1 Index and Length

**Python**

```python
A = [10, 20, 30]
n = len(A)
first = A[0]
last  = A[n - 1]
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

- Because `-` is not an operator, `n - 1` is written `diff of n and 1`.
- Note that indexing reads as `item INDEX in ARRAY`, not `ARRAY[INDEX]`.

---

## 6. Objects (Dicts)

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

Object access uses the same `item KEY in OBJ` syntax as array access.
Keys are strings.

---

## 7. Strings Are Arrays

In Python `str` and `list` are distinct types. In Bridget a string **is** a
character-code array, so all array operations apply directly.

**Python**

```python
s = list("hello".encode())   # [104, 101, 108, 108, 111]
s[0] = ord("H")
for c in " world".encode():
    s.append(c)
# decode back: bytes(s).decode() == "Hello world"
```

**Bridget**

```bridget
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

- `item 0 in "H"` returns the character code of `'H'` (72).
- Appending a character code to a string extends it, just like appending to an
  array.

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
Remember that flag is Yes
Remember that result is 0

When flag is Yes, then:
  Remember that result is 1
But, if not:
  Remember that result is 2
End when
```

### 8.1 Comparison Operators → Phrases

Bridget uses **no comparison symbols** (`==`, `!=`, `<`, `>`, `<=`, `>=`).

| Python | Bridget |
|--------|---------|
| `a == b` | `a is b` |
| `a != b` | `a is not b` |
| `a < b`  | `a is less than b` |
| `a > b`  | `a is more than b` |
| `a <= b` | `a is at least b` |
| `a >= b` | `a is at most b` |
| `a in xs` | `a is in xs` |
| `a not in xs` | `a is not in xs` |

> **`is at least` and `is at most` are counterintuitive.**
> In everyday English "at least" implies ≥ and "at most" implies ≤,
> but in Bridget **they are reversed**:
>
> | Bridget | Python equivalent |
> |---------|-------------------|
> | `When i is at least m, then:` | `if i <= m:` |
> | `When n is at most 0, then:` | `if n >= 0:` |

**Python**

```python
fruits = ["apple", "banana", "cherry"]
found   = 1 if "banana" in fruits else 0
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

### 8.2 Multi-Branch (elif)

Bridget has no `elif`. Nest `When` inside `But, if not:`.

**Python**

```python
if grade > 90:
    label = "A"
elif grade > 75:
    label = "B"
else:
    label = "C"
```

**Bridget**

```bridget
When grade is more than 90, then:
  Remember that label is "A"
But, if not:
  When grade is more than 75, then:
    Remember that label is "B"
  But, if not:
    Remember that label is "C"
  End when
End when
```

---

## 9. Loops

Bridget has only a **count-based loop** — no `while` and no `for x in xs`.

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

| Python | Bridget |
|--------|---------|
| `for _ in range(N):` | `Do this N times:` … `End do` |
| `break` | `Leave the loop` |
| `continue` | *(not available — use inverted condition or skip flag)* |

To iterate over an array, manage an index variable yourself:

**Python**

```python
for i in range(len(arr)):
    process(arr[i])
```

**Bridget**

```bridget
Remember that i is 0
Do this arr's length times:
  Remember that val is item i in arr
  # ... process val ...
  Increase i
End do
```

Simulating `while` — use a large repeat count and `Leave the loop`:

**Python**

```python
while b != 0:
    a, b = b, a % b
```

**Bridget**

```bridget
Use the standard library

Do this a times:
  When b is 0, then:
    Leave the loop
  End when
  Remember that r is remainder of a and b
  Remember that a is b
  Remember that b is r
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

| Python | Bridget |
|--------|---------|
| `def f(a, b):` | `This is how to f of a and b:` |
| `return x` | `The answer is x` |
| `return` (no value) | `Stop here` |
| `f(a, b)` (call) | `f of a and b` |
| `f(a, b, c)` (call) | `f of a and b and c` |
| `f()` (no args) | `f, do it` |

- Variables defined inside a function are **local** (same as Python).
- At least one parameter is required in a function definition.

### 10.2 Implicit Return (Constructor Pattern)

In Python a function without `return` returns `None`. In Bridget it returns
an **object containing all local variables** — useful as a lightweight constructor.

**Python equivalent**

```python
def point(x, y):
    return {"x": x, "y": y}

O = point(3, 5)
assert O["x"] == 3
```

**Bridget**

```bridget
This is how to point of x and y:
  # No explicit return → returns {"x": x, "y": y}
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
  But, if not:
    The answer is product of n and (fact of (diff of n and 1))
  End when
Now you know

>>> fact of 5
120
```

Because `*` and `-` are not operators, `n * fact(n-1)` becomes
`product of n and (fact of (diff of n and 1))`.

---

## 11. Standard Library

Python has rich built-in operators and functions. Bridget **uses no arithmetic
symbols** — everything goes through library functions.
Declare `Use the standard library` at the top.

### 11.1 Arithmetic

| Python | Bridget |
|--------|---------|
| `a + b + c` | `sum of a and b and c` (array also OK: `sum of [a,b,c]`) |
| `a - b` | `diff of a and b` |
| `a * b` | `product of a and b` |
| `a // b` | `quotient of a and b` (floor division for int/int) |
| `a % b` | `remainder of a and b` |

> **`quotient` with two integers is floor division.** When you need a float
> result, convert at least one operand: `quotient of (tofloat of a) and (tofloat of b)`.

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

Because Bridget has no `while`, simulate it with a large repeat count and
`Leave the loop`.

### 11.2 Math Functions

| Python | Bridget |
|--------|---------|
| `abs(x)` | `abs of x` |
| `math.sqrt(x)` | `sqrt of x` (always float) |
| `max(a, b, ...)` / `max(xs)` | `max of a and b and …` / `max of xs` |
| `min(a, b, ...)` / `min(xs)` | `min of a and b and …` / `min of xs` |
| `random.random()` | `random, do it` |

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

| Python | Bridget |
|--------|---------|
| `int(x)` | `toint of x` |
| `float(x)` | `tofloat of x` |
| `str(x)` | `tostring of x` |
| `list("Hi".encode())` → `[72,105]` | `toarray of "Hi"` |

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

### 11.4 Type Check

| Python | Bridget |
|--------|---------|
| `isinstance(x, bool)` | `isbool of x` |
| `isinstance(x, int)` | `isint of x` |
| `isinstance(x, float)` | `isfloat of x` |
| `isinstance(x, str)` | `isstring of x` |
| `isinstance(x, list)` | `isarray of x` |
| `isinstance(x, dict)` | `isobject of x` |

```bridget
Use the standard library

>>> isint of 42
Yes
>>> isstring of "hello"
Yes
>>> isint of "42"
No
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

**Bridget** — counter-based approach avoids remainder calls entirely:

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

`dist <= 1` (point inside the unit circle) maps to `dist is at least 1` —
remember that `is at least` means `<=` in Bridget.

---

## 14. What Python Has That Bridget Does Not

| Python feature | Bridget equivalent / workaround |
|----------------|----------------------------------|
| `+`, `-`, `*`, `/`, `%` operators | `sum`, `diff`, `product`, `quotient`, `remainder` |
| `==`, `!=`, `<`, `>`, `<=`, `>=` | `is`, `is not`, `is less than`, `is more than`, `is at least`(≤), `is at most`(≥) |
| `while cond:` | `Do this N times:` + `Leave the loop` |
| `for x in xs:` | Index loop with `Increase i` |
| `elif` | Nested `When` inside `But, if not:` |
| `continue` | Inverted condition or skip-flag variable |
| `return` (no value) | `Stop here` |
| No `return` → `None` | No explicit return → **object of all local vars** |
| `arr.pop()` / `del arr[i]` | Not available — manage a logical-size variable |
| Classes, exceptions, modules | Not available — Bridget is intentionally minimal |

---

## 15. Summary

| Concept | Python | Bridget |
|---------|--------|---------|
| Assign | `x = 1` | `Remember that x is 1` |
| Read index | `arr[i]` | `item i in arr` |
| Write index | `arr[i] = v` | `Remember that item i in arr is v` |
| Append | `arr.append(x)` | `Add arr to x` |
| Length | `len(arr)` | `arr's length` |
| If | `if cond:` | `When cond, then:` … `End when` |
| Else | `else:` | `But, if not:` |
| For N | `for _ in range(N):` | `Do this N times:` … `End do` |
| Break | `break` | `Leave the loop` |
| Def | `def f(a, b):` | `This is how to f of a and b:` … `Now you know` |
| Return | `return x` | `The answer is x` |
| Call | `f(a, b)` | `f of a and b` |
| Call (0 args) | `f()` | `f, do it` |
| Add | `a + b` | `sum of a and b` |
| Multiply | `a * b` | `product of a and b` |

For the full formal grammar see `ebnf_en.md`, complete stdlib signatures see
`apidoc_en.md`, and quick syntax reference see `spec_en.md`.
