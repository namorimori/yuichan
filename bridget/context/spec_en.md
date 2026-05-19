# Bridget Language Specification

Bridget is a plain-English programming language built on the Yui runtime.
Programs read like structured English instructions, with keywords replacing
all mathematical symbols and operators.

---

## 1. Lexical Rules

| Element | Details |
|---------|---------|
| Whitespace | space, tab |
| Newline | `\n` (statement separator) |
| Line comment | `#` to end of line |
| Identifier | `/[A-Za-z_][A-Za-z0-9_]*/`, or any chars wrapped in backticks `` `…` `` |

One statement per line is the norm. Multi-word identifiers that contain
non-alphanumeric characters must be wrapped in backticks (e.g. `` `my-var` ``).

---

## 2. Type System

All values belong to one of seven types.

| Type | Literal |
|------|---------|
| Null | `Nothing` / `nothing` / `null` |
| Boolean | `Yes` / `yes` / `true` · `No` / `no` / `false` |
| Integer | `42` |
| Float | `3.14` (displayed with 6 decimal places) |
| String | `"hello"`, `"x={x}"` |
| Array | `[1, 2, 3]` |
| Object | `{"x": 1, "y": 2}` |

- **Strings** are stored internally as **arrays of character codes (int)**, so all array operations (indexing, length, append) apply equally to strings.
- **Integers** are stored internally as **bit arrays (LSB first)**, so `item 0 in 6` returns `0`, `item 1 in 6` returns `1`, and `6's length` returns `3`. Bit operations can be implemented as array manipulation, or via the standard library (`bitand`, `bitor`, etc.).
- Array equality is recursive; a character-code array and a string compare equal (`[72,105]` == `"Hi"`), and a bit array and an integer compare equal (`[0,1,1]` == `6`).

---

## 3. Expressions

Expressions are evaluated to a single value and may be nested freely.

### 3.1 Literals

See the type table in §2. Floats display as 6 decimal places (`3.140000`).

### 3.2 String Interpolation

Embed an expression inside a string with `{expr}`. Escape `{` and `"` as `\{` and `\"`. `\\`, `\n`, `\t` are also supported.

```
Remember that name is "Bridget"
Remember that msg is "Hello, {name}!"
```

### 3.3 Length Property

```
EXPR's length
```

Returns the number of elements in an array or string.

```
Remember that n is arr's length
When current_word's length is more than 0, then:
```

### 3.4 Unary Minus

`-expr` negates a numeric value. May be written directly on a literal: `Remember that y is -2`.

### 3.5 Arithmetic

`+`, `-`, `*`, `/`, `%` **operators are not used in Bridget**. Use standard library functions instead.

| Function | Meaning |
|----------|---------|
| `sum of x and y and …` | sum (array argument also accepted) |
| `diff of x and y and …` | difference |
| `product of x and y and …` | product |
| `quotient of x and y` | quotient (floor division for integers) |
| `remainder of x and y` | remainder |

### 3.6 Array Index and Object Property

Read an element with `item INDEX in ARRAY`. **The index comes before the array** — the reverse of `ARRAY[INDEX]`.

```
Remember that val is item i in arr        # read arr[i]
Remember that item i in arr is val        # write arr[i]  (as assignment target)
Remember that ch is item 0 in "hello"     # char code of 'h' = 104
```

Object properties use a string key:

```
Remember that obj is {"x": 1, "y": 2}
Remember that x is item "x" in obj
```

### 3.7 Function Application

```
funcname of arg                   # one argument
funcname of arg1 and arg2         # two arguments
funcname of arg1 and arg2 and arg3
funcname, do it                   # zero arguments
```

---

## 4. Statements

### 4.1 Assignment

Bind a value to a name. Re-assigning overwrites the previous value.

```
Remember that NAME is EXPR
```

To write into an indexed position:

```
Remember that item j in words is item next_j in words
```

### 4.2 Increment / Decrement

```
Increase NAME
Decrease NAME
```

Both change the variable by exactly 1. `by 1` may be appended optionally.

### 4.3 Append

```
Add ARRAY to ELEMENT
```

**The array is the first operand; the element to append is the second.** This is the reverse of the natural English reading "add X to Y".

```
Add result to item i in string    # appends (item i in string) to result
Add current_word to char          # appends char to current_word
```

Strings accept appending character codes in the same way as arrays.

### 4.4 Conditional

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

`But, if not:` is optional. For elif-style chaining, nest `When` inside `But, if not:`.

#### Comparison Operators

`==`, `!=`, `<`, `>`, `<=`, `>=` **symbols are not used**. Use the following phrases:

| Bridget phrase | Operator | Example |
|----------------|----------|---------|
| `is` | `==` | `When x is 0, then:` |
| `is not` | `!=` | `When x is not 0, then:` |
| `is less than` | `<` | `When r is less than b, then:` |
| `is more than` | `>` | `When x is more than 10, then:` |
| `is at least` | `<=` | `When i is at least m, then:` → `if i <= m` |
| `is at most` | `>=` | `When n is at most 0, then:` → `if n >= 0` |
| `is in` | `in` | `When x is in arr, then:` |
| `is not in` | `not in` | `When x is not in arr, then:` |

> **`is at least` and `is at most` are counterintuitive.**
> In everyday English "at least" implies ≥ and "at most" implies ≤,
> but in Bridget **`is at least` means `<=`** and **`is at most` means `>=`**.
>
> ```
> When i is at least m, then:    # if i <= m   (NOT i >= m)
> When n is at most 100, then:   # if n >= 100 (NOT n <= 100)
> ```

### 4.5 Repeat

```
Do this N times:
   …
End do
```

`N` is an expression evaluated once before the loop begins.
Exit early with `Leave the loop`.

```
Do this length times:
   Remember that val is item i in arr
   When val is 0, then:
      Leave the loop
   End when
   Increase i
End do
```

### 4.6 Function Definition

```
This is how to NAME of PARAM1 and PARAM2 …:
   …
   The answer is EXPR
Now you know
```

- At least one parameter is required.
- **Return a value**: `The answer is EXPR`
- **Return without value**: `Stop here`
- Variables defined inside a function are **local** and invisible outside.
- **Implicit return**: if the body ends without `The answer is` or `Stop here`, the runtime returns an object containing all local variables (constructor-like pattern).

```
This is how to add of x and y:
   Remember that result is sum of x and y
   The answer is result
Now you know
>>> add of 3 and 4
7
```

### 4.7 Doctest (Assert)

```
>>> EXPR
expected_literal
```

Evaluates `EXPR` and checks it equals the literal on the next line. Follows Python doctest conventions.

### 4.8 Import

```
Use the standard library
```

Registers all standard library functions in the current environment. Must appear before any call to those functions.

### 4.9 Pass

```
Do nothing
```

A no-op placeholder, useful when a branch requires at least one statement.

### 4.10 Print Expression

A bare expression statement evaluates and prints its result automatically.

---

## 5. Block

A block is a sequence of statements sharing the same indentation level (2 spaces per level).
Blocks have no explicit delimiter of their own; they are closed by the enclosing
construct's closing keyword.

| Construct | Opens with | Closes with |
|-----------|------------|-------------|
| If | `When …, then:` | `End when` |
| Else | `But, if not:` | (same `End when`) |
| Loop | `Do this N times:` | `End do` |
| Function | `This is how to … of …:` | `Now you know` |

---

## 6. Standard Library (Summary)

Declare `Use the standard library` to enable these functions.

| Category | Functions |
|----------|-----------|
| Math | `abs of x` · `sqrt of x` · `random, do it` |
| Arithmetic | `sum` · `diff` · `product` · `quotient` · `remainder` · `max` · `min` |
| Bitwise | `bitand` · `bitor` · `bitxor` · `bitnot` · `lshift` · `rshift` |
| Convert | `toint` · `tofloat` · `tostring` · `toarray` |
| Type check | `isbool` · `isint` · `isfloat` · `isstring` · `isarray` · `isobject` |

See `apidoc_en.md` for full signatures and examples.

---

## 7. References

- `apidoc_en.md` — standard library full reference
- `ebnf_en.md` — formal grammar in extended BNF
- `CLAUDE.md` — runtime implementation notes
