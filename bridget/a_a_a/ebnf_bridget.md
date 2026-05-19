# Bridget Syntax — Extended BNF Grammar Definition

This document defines the grammar of Yui language using the **bridget** syntax dialect in Extended BNF.

## Notation

- `A = B` — production rule
- `A | B` — alternation
- `[ A ]` — zero or one occurrence (optional)
- `{ A }` — zero or more repetitions
- `"..."` — terminal symbol (literal string)
- `/.../` — terminal defined by regular expression
- Whitespace (space, tab) may appear between lexical elements. Statements are separated by newline `LF`.

---

## 1. Program

```
program         = { statement } ;
statement       = ( import_stmt
                  | assert_stmt
                  | assignment
                  | increment
                  | decrement
                  | append
                  | if_stmt
                  | repeat_stmt
                  | funcdef
                  | return_stmt
                  | break_stmt
                  | pass_stmt
                  | print_stmt
                  | expr_stmt ) , LF ;
LF              = /\n/ ;
```

---

## 2. Lexical Elements

```
whitespace      = /[ \t\r　]/ ;
line_comment    = "#" , { /[^\n]/ } ;

identifier      = simple_name | extra_name ;
simple_name     = /[A-Za-z_][A-Za-z0-9_]*/ ;
extra_name      = "`" , { /[^`]/ } , "`" ;

integer         = /[0-9]+/ ;
float_lit       = /[0-9]+/ , "." , /[0-9]+/ ;
number          = float_lit | integer ;

string          = '"' , { string_part } , '"' ;
string_part     = string_char | string_escape | string_interp ;
string_char     = /[^"\\{]/ ;
string_escape   = "\\" , /./ ;
string_interp   = "{" , expression , "}" ;
```

---

## 3. Type Literals

```
literal         = null_lit
                | bool_lit
                | number
                | string
                | array_lit
                | object_lit ;

null_lit        = "nothing" | "null" | "Nothing" ;
bool_lit        = "yes" | "true" | "Yes"
                | "no" | "false" | "No" ;

array_lit       = "[" , [ expression , { "," , expression } ] , "]" ;

object_lit      = "{" , [ key_value , { "," , key_value } ] , "}" ;
key_value       = string , ":" , expression ;
```

Note: `no` and `false` are only recognized as boolean literals when not followed by an identifier character, preventing conflicts with variable names like `nothing`.

---

## 4. Expressions

Operator precedence from highest to lowest: primary → indexing / function call (postfix) → unary `-` → length → base expression.

```
expression      = length_expr | unary_expr ;

length_expr     = postfix_expr , "'s" , "length" ;

unary_expr      = [ "-" ] , postfix_expr ;

postfix_expr    = primary_expr , { postfix_op } ;
postfix_op      = index_suffix
                | call_suffix ;

index_suffix    = "item" , expression , "in" , primary_expr ;
call_suffix     = "of" , arg_list
                | "," , "do" , "it" ;

arg_list        = expression , { "and" , expression } ;

primary_expr    = literal
                | identifier
                | "(" , expression , ")" ;
```

Notes:
- In the bridget dialect, infix binary operators (`+ - * / % == != < <= > >=`) are **not available**. Arithmetic and comparisons use standard-library functions (`sum`, `diff`, `product`, `quotient`, `remainder`, etc.) and the `When ... then:` conditional syntax.
- Function calls use prefix notation: `sum of a and b` instead of `a + b`.
- Array indexing is written `item i in A` rather than `A[i]`.
- `A's length` is the length of array or string `A`.
- Function calls and indexing can be chained freely: e.g., `item 0 in (f of x)`.

---

## 5. Assignment, Increment, Decrement, Append

```
assignment      = "Remember" , "that" , assign_target , "is" , expression ;
assign_target   = identifier
                | "item" , expression , "in" , identifier ;

increment       = "Increase" , assign_target , [ "by" , "1" ] ;
decrement       = "Decrease" , assign_target , [ "by" , "1" ] ;

append          = "Add" , assign_target , "to" , expression ;
```

Note: `Add A to x` appends `x` to the array `A`. The container is written first.

---

## 6. Conditionals

```
if_stmt         = "When" , condition , "," , "then" , ":" , block ,
                  [ "But" , "," , "if" , "not" , ":" , block ] ,
                  "End" , "when" ;

condition       = expression , cmp_op , expression ;

cmp_op          = "is" /\s/             (* == *)
                | "is" , "not" /\s/     (* != *)
                | "is" , "less" , "than"   (* <  *)
                | "is" , "at" , "least"    (* <= *)
                | "is" , "more" , "than"   (* >  *)
                | "is" , "at" , "most"     (* >= *)
                | "is" , "in" /\s/         (* element of *)
                | "is" , "not" , "in" ;    (* not element of *)
```

Comparison keyword reference:

| Bridget keyword         | Operator | Meaning                    |
|-------------------------|----------|----------------------------|
| `is`                    | `==`     | equal to                   |
| `is not`                | `!=`     | not equal to               |
| `is less than`          | `<`      | strictly less than         |
| `is at least`           | `<=`     | less than or equal to      |
| `is more than`          | `>`      | strictly greater than      |
| `is at most`            | `>=`     | greater than or equal to   |
| `is in`                 | `∈`      | element of array/string    |
| `is not in`             | `∉`      | not element of             |

> **Note:** `is at least` means `≤` and `is at most` means `≥`. These names are counterintuitive compared to standard English but are fixed by the bridget dialect specification.

---

## 7. Loops

```
repeat_stmt     = "Do" , "this" , expression , "times" , ":" , block , "End" , "do" ;
break_stmt      = "Leave" , "the" , "loop" ;
```

There is no `while` loop. Simulate it with a large repeat count and `Leave the loop` (break).

---

## 8. Function Definitions and Return

```
funcdef         = "This" , "is" , "how" , "to" , identifier ,
                  ( funcdef_with_args | funcdef_noarg ) , ":" , block ,
                  "Now" , "you" , "know" ;

funcdef_with_args = "of" , identifier , { "and" , identifier } ;
funcdef_noarg     = noarg_marker ;
noarg_marker      = /[^o][^f]/ ;   (* any two chars that don't spell "of"; conventionally "^^" *)

return_stmt     = return_value | return_none ;
return_value    = "The" , "answer" , "is" , expression ;
return_none     = "Stop" , "here" ;
```

If the function body ends without a `The answer is` statement, the function's local variables are implicitly returned as an object (bridget's implicit-object return).

No-argument function syntax:
```bridget
This is how to greet ^^:
   The answer is "Hello!"
Now you know
```

The `^^` marker satisfies the `noarg_marker` pattern. Any two-character sequence not spelling `of` is accepted; `^^` is the conventional choice.

---

## 9. Imports

```
import_stmt     = import_standard | import_named ;
import_standard = "Use" , "the" , "standard" , "library" ;
import_named    = "Use" , identifier ;
```

---

## 10. Doctest Assertions

```
assert_stmt     = ">>>" , expression , LF , expected_value ;
expected_value  = literal ;
```

The expression after `>>>` is evaluated; its result must equal the literal on the following line. Assertion syntax matches Python doctest.

Note: function calls in doctest lines use bridget syntax:
```bridget
>>> sum of 3 and 4
7
>>> greet, do it
"Hello!"
```

---

## 11. Print, Pass, and Expression Statements

```
print_stmt      = "Now" , "," , expression ;
pass_stmt       = "Do" , "nothing" ;
expr_stmt       = expression ;
```

A standalone `expr_stmt` evaluates the expression and prints its value automatically (REPL-style behaviour).

---

## 12. Blocks

Blocks are introduced by `:` and terminated by the matching end keyword of the enclosing construct:

| Construct         | Block opener          | Block terminator  |
|-------------------|-----------------------|-------------------|
| `if_stmt`         | `When ..., then:`     | `End when`        |
| `if_stmt` (else)  | `But, if not:`        | `End when`        |
| `repeat_stmt`     | `Do this N times:`    | `End do`          |
| `funcdef`         | `This is how to ...`  | `Now you know`    |

```
block           = ":" , LF , { "  " , statement } ;
```

The standard indentation is two spaces per nesting level. Indentation is not enforced by the parser but is required for readability and is generated consistently by the code generator.

---

## 13. Standard Library Functions (Reference)

`Use the standard library` must appear at the top of the program before any stdlib call.

| Function                   | Signature                     | Description                         |
|----------------------------|-------------------------------|-------------------------------------|
| `sum of a and b`           | `sum(a, b, ...)` or `sum([...])` | Addition (variadic)              |
| `diff of a and b`          | `diff(a, b)`                  | Subtraction: `a − b`                |
| `product of a and b`       | `product(a, b, ...)` or `product([...])` | Multiplication         |
| `quotient of a and b`      | `quotient(a, b)`              | Integer/floor division              |
| `remainder of a and b`     | `remainder(a, b)`             | Modulo                              |
| `abs of x`                 | `abs(x)`                      | Absolute value                      |
| `sqrt of x`                | `sqrt(x)`                     | Square root (returns float)         |
| `max of a and b`           | `max(a, b, ...)` or `max([...])` | Maximum value                    |
| `min of a and b`           | `min(a, b, ...)` or `min([...])` | Minimum value                    |
| `random, do it`            | `random()`                    | Random float in [0, 1)              |
| `toint of x`               | `toint(x)`                    | Convert to integer                  |
| `tofloat of x`             | `tofloat(x)`                  | Convert to float                    |
| `tostring of x`            | `tostring(x)`                 | Convert to string                   |
| `toarray of x`             | `toarray(x)`                  | Convert string to char-code array   |
| `isint of x`               | `isint(x)`                    | Is integer? (yes/no)                |
| `isfloat of x`             | `isfloat(x)`                  | Is float? (yes/no)                  |
| `isstring of x`            | `isstring(x)`                 | Is string? (yes/no)                 |
| `isarray of x`             | `isarray(x)`                  | Is array? (yes/no)                  |
| `isobject of x`            | `isobject(x)`                 | Is object? (yes/no)                 |
| `isbool of x`              | `isbool(x)`                   | Is boolean? (yes/no)                |
