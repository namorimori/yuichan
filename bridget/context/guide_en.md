# Bridget Programming Guide

Bridget is a plain-English programming language built on the Yui runtime.
Programs read like structured instructions: no math symbols, no operators —
everything is spelled out in words.

---

## 1. First Program

A bare expression statement evaluates and prints its result.

```bridget
# Print a greeting
"Hello, world!"
```

Lines beginning with `#` are comments and are ignored.

---

## 2. Variables, Increment, and Decrement

`Remember that NAME is EXPR` binds a value to a name.
Re-assigning overwrites the previous value.

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

`>>> EXPR` followed by an expected literal on the next line is a **doctest** —
it asserts that the expression equals the literal (Python doctest convention).

---

## 3. Types and Literals

Every value belongs to exactly one of seven types.

| Type    | Literal |
|---------|---------|
| Null    | `Nothing` / `nothing` / `null` |
| Boolean | `Yes` / `yes` / `true` · `No` / `no` / `false` |
| Integer | `42` |
| Float   | `3.14` (displayed with 6 decimal places) |
| String  | `"hello"`, `"x={x}"` |
| Array   | `[1, 2, 3]` |
| Object  | `{"x": 1, "y": 2}` |

- **Strings** are stored internally as **character-code arrays**, so all array
  operations (indexing, length, append) work on strings too.
- **Integers** are stored as **bit arrays (LSB first)**: `item 0 in 6` → `0`,
  `item 1 in 6` → `1`, `6's length` → `3`.

---

## 4. String Interpolation

Embed any expression inside a string with `{expr}`.

```bridget
Remember that name is "Bridget"
Remember that age is 3
Remember that msg is "Hello, {name}! You are {age} years old."
msg

>>> msg
"Hello, Bridget! You are 3 years old."
```

Escape `{` as `\{` and `"` as `\"`. `\\`, `\n`, `\t` are also supported.

---

## 5. Arrays

`[...]` creates an array. `Add ARRAY to ELEMENT` appends an element to an array.

> **Watch out:** the syntax is `Add ARRAY to ELEMENT` — **array first, element second**.
> This is the reverse of the natural English reading "add X to Y".

```bridget
Remember that A is [1, 2, 3]

# Append 0 to the end of A
Add A to 0

# Increase the first element by 1
Increase item 0 in A

>>> A's length
4
```

### 5.1 Indexing and Length

- `item i in arr` — reads element at index `i` (0-based)
- `arr's length` — number of elements

```bridget
Use the standard library

Remember that A is [10, 20, 30]
Remember that n is A's length

Remember that first is item 0 in A
Remember that last is item (diff of n and 1) in A

>>> first
10
>>> last
30

# Write to a specific index
Remember that item 1 in A is 200
>>> item 1 in A
200
```

---

## 6. Objects

`{"key": value, ...}` creates an object. Keys are strings.

```bridget
Remember that O is {"x": 0, "y": 0}
Remember that item "x" in O is 1
Remember that item "y" in O is 2

>>> item "x" in O
1
>>> item "y" in O
2
```

---

## 7. Strings Are Arrays

Because strings are character-code arrays, you can index them and append to them.

```bridget
Remember that s is "hello"

# Overwrite the first character with 'H'
Remember that item 0 in s is item 0 in "H"

# Append " world" character by character
Remember that t is " world"
Remember that i is 0
Do this t's length times:
  Add s to item i in t
  Increase i
End do

>>> s
"Hello world"
```

---

## 7.5 Integers Are Bit Arrays

Integers are stored as bit arrays with the LSB first, so array operations apply.

```bridget
# 6 in binary is 110 → stored as [0, 1, 1] (LSB first)
>>> item 0 in 6
0
>>> item 1 in 6
1
>>> item 2 in 6
1
>>> 6's length
3
```

A character-code array and its string compare equal, and a bit array and its
integer compare equal:

```bridget
>>> [0, 1, 1] is 6
Yes
```

### Bit AND Example

```bridget
This is how to bits_and of A and B:
  Remember that n is A's length
  When B's length is less than n, then:
    Remember that n is B's length
  End when
  Remember that i is 0
  Remember that X is 0
  Do this n times:
    Remember that x is 0
    When item i in A is 1, then:
      When item i in B is 1, then:
        Remember that x is 1
      End when
    End when
    Add X to x
    Increase i
  End do
  The answer is X
Now you know

>>> bits_and of 6 and 5
4
>>> bits_and of 3 and 1
1
```

---

## 8. Conditionals

```
When CONDITION, then:
  …
End when

When CONDITION, then:
  …
But, if not:
  …
End when
```

`But, if not:` is optional. For elif-style chains, nest `When` inside `But, if not:`.

```bridget
Remember that flag is Yes
Remember that result is 0

When flag is Yes, then:
  Remember that result is 1
But, if not:
  Remember that result is 2
End when

>>> result
1
```

### 8.1 Comparison Phrases

`==`, `!=`, `<`, `>`, `<=`, `>=` symbols are **not used** in Bridget.

| Bridget phrase | Operator | Example |
|----------------|----------|---------|
| `is` | `==` | `When x is 0, then:` |
| `is not` | `!=` | `When x is not 0, then:` |
| `is less than` | `<` | `When r is less than b, then:` |
| `is more than` | `>` | `When x is more than 10, then:` |
| `is at least` | `<=` | `When i is at least m, then:` |
| `is at most` | `>=` | `When n is at most 0, then:` |
| `is in` | `in` | `When x is in arr, then:` |
| `is not in` | `not in` | `When x is not in arr, then:` |

> **`is at least` and `is at most` are counterintuitive.**
> In everyday English "at least" suggests ≥ and "at most" suggests ≤,
> but in Bridget they are **reversed**:
>
> ```
> When i is at least m, then:    # if i <= m   (NOT i >= m)
> When n is at most 0, then:     # if n >= 0   (NOT n <= 0)
> ```

### 8.2 Multi-Branch (elif)

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

`Do this N times: ... End do` executes a block N times.
Exit early with `Leave the loop`.

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

---

## 10. Functions

### 10.1 Definition and Return

```
This is how to NAME of PARAM1 and PARAM2 …:
  …
  The answer is EXPR
Now you know
```

`The answer is EXPR` returns a value. `Stop here` returns without a value.
Variables defined inside a function are **local** and invisible outside.

```bridget
This is how to succ of n:
  Increase n
  The answer is n
Now you know

>>> succ of 0
1
```

### 10.2 Calling Functions

```
funcname of arg                     # one argument
funcname of arg1 and arg2           # two arguments
funcname of arg1 and arg2 and arg3  # three arguments
funcname, do it                     # zero arguments
```

### 10.3 Implicit Return (Constructor Pattern)

If the body ends without `The answer is` or `Stop here`, the runtime returns an
object containing all local variables.

```bridget
This is how to point of x and y:
  # No explicit return → returns {"x": x, "y": y}
Now you know

Remember that O is point of 3 and 5

>>> item "x" in O
3
```

### 10.4 Recursion

```bridget
Use the standard library

This is how to fact of n:
  When n is 0, then:
    The answer is 1
  But, if not:
    The answer is product of n and (fact of (diff of n and 1))
  End when
Now you know

>>> fact of 0
1
>>> fact of 5
120
```

---

## 11. Standard Library

Declare `Use the standard library` at the top to enable library functions.
`+`, `-`, `*`, `/`, `%` **operators are not used** — call functions instead.

### 11.1 Arithmetic

| Function | Meaning |
|----------|---------|
| `sum of x and y and …` | Sum (array argument also accepted) |
| `diff of x and y and …` | Difference |
| `product of x and y and …` | Product |
| `quotient of x and y` | Quotient (floor division for integers) |
| `remainder of x and y` | Remainder |

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
>>> gcd of 100 and 75
25
```

> **Integer division is floor division.** When you need a float result, convert
> at least one operand first: `quotient of (tofloat of a) and (tofloat of b)`.

### 11.2 Math Functions

| Function | Result |
|----------|--------|
| `abs of x` | Absolute value |
| `sqrt of x` | Square root (always float) |
| `max of x and y and …` | Maximum (array accepted) |
| `min of x and y and …` | Minimum (array accepted) |
| `random, do it` | Random float in [0, 1) |

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

| Function | Result |
|----------|--------|
| `toint of x` | Integer |
| `tofloat of x` | Float |
| `tostring of x` | String |
| `toarray of x` | Character-code array (string) or key array (object) |

```bridget
Use the standard library

>>> toint of "42"
42
>>> toint of 3.700000
3
>>> tofloat of 5
5.000000
>>> tostring of 42
"42"
>>> toarray of "Hi"
[72, 105]
```

### 11.4 Type Check

| Function | Returns `Yes` when… |
|----------|---------------------|
| `isbool of x` | x is boolean |
| `isint of x` | x is integer |
| `isfloat of x` | x is float |
| `isstring of x` | x is string |
| `isarray of x` | x is array |
| `isobject of x` | x is object |

```bridget
Use the standard library

>>> isint of 42
Yes
>>> isstring of "hello"
Yes
>>> isint of "42"
No
```

### 11.5 Bitwise Functions

| Function (alias) | Operation |
|------------------|-----------|
| `bitand` (`band`) | AND |
| `bitor` (`bor`) | OR |
| `bitxor` (`bxor`) | XOR |
| `bitnot` (`bnot`) | NOT (1 argument) |
| `lshift` | Left shift |
| `rshift` | Right shift |

```bridget
Use the standard library

>>> bitand of 6 and 3
2
>>> lshift of 1 and 4
16
>>> rshift of 16 and 4
1
```

---

## 12. Common Pitfalls

### `Add ARRAY to ELEMENT` — order is reversed

The array comes first, the new element second. This is the opposite of natural
English "add X to Y":

```bridget
Remember that result is []
Add result to 42       # appends 42 to result
Add result to "hello"  # appends "hello" to result
```

### `is at least` means `<=`, `is at most` means `>=`

Always double-check the direction when writing range guards:

```bridget
# Loop while i <= last_index:
When i is at least (diff of n and 1), then:
  Leave the loop
End when
```

### No `continue` — use inverted condition or skip flag

Bridget has `Leave the loop` (break) but no continue equivalent.

**Option A — invert the condition:**
```bridget
Do this n times:
  Remember that x is item i in arr
  When x is more than 0, then:    # skip when x <= 0
    # body here
  End when
  Increase i
End do
```

**Option B — skip flag:**
```bridget
Do this n times:
  Remember that x is item i in arr
  Remember that skip is No
  When x is at most 0, then:
    Remember that skip is Yes
  End when
  When skip is No, then:
    # body here
  End when
  Increase i
End do
```

### No pop/remove — manage a logical size separately

Bridget arrays support append but not removal. When you need a resizable
stack or queue, track a logical size variable and overwrite slots on push:

```bridget
Remember that stack is []
Remember that top is 0

# Push x onto the stack
This is how to push of x:
  When top is at least stack's length, then:
    Add stack to x
  But, if not:
    Remember that item top in stack is x
  End when
  Increase top
Now you know
```

---

## 13. Full Example: FizzBuzz

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

## 14. Full Example: Monte Carlo π Estimate

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

---

## 15. Summary

- **Assignment**: `Remember that NAME is EXPR`
- **Index**: `item INDEX in ARRAY` (index before array)
- **Append**: `Add ARRAY to ELEMENT` (array before element)
- **Condition**: `When COND, then: … End when`; `But, if not:` for else
- **Comparison**: `is` / `is not` / `is less than` / `is more than` /
  `is at least` (≤) / `is at most` (≥)
- **Loop**: `Do this N times: … End do`; `Leave the loop` to break
- **Function**: `This is how to NAME of PARAMS: … The answer is EXPR / Now you know`
- **Arithmetic**: `sum`, `diff`, `product`, `quotient`, `remainder` — no `+`, `-`, `*`, `/`, `%`
- **Doctest**: `>>> EXPR` then expected literal on the next line

For the full formal grammar see `ebnf_en.md`, and for complete stdlib signatures
see `apidoc_en.md`.
