# Wenyan Syntax — Extended BNF Grammar Definition

This document defines the grammar of the Yui language using the **wenyan** (Classical Chinese) syntax dialect in Extended BNF.

## Notation

- `A = B` — production rule
- `A | B` — alternation
- `[ A ]` — zero or one occurrence (optional)
- `{ A }` — zero or more repetitions
- `"..."` — terminal symbol (literal string)
- `/.../` — terminal defined by regular expression
- Whitespace (space, tab, fullwidth space) may appear between lexical elements. Statements are separated by newline `LF`.

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
line_comment    = "注" , [ "、" | "。" ] , { /[^\n]/ } ;
block_comment   = "注始" , { /.*/ } , "注終" ;

identifier      = simple_name | extra_name | special_name ;
simple_name     = /[A-Za-z_][A-Za-z0-9_]*/ ;
extra_name      = "`" , { /[^`]/ } , "`" ;
special_name    = /[^\s\[\]()"',+\-*\/%=!<>]+/ ;

integer         = /[0-9]+/ ;
float_lit       = /[0-9]+/ , "." , /[0-9]+/ ;
number          = float_lit | integer ;

string          = "「" , { string_part } , "」" ;
string_part     = string_char | string_escape | string_interp ;
string_char     = /[^」\\{]/ ;
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

null_lit        = "無" | "null" ;
bool_lit        = "然" | "true"
                | "否" | "false" ;

array_lit       = "[" , [ expression , { "," , expression } ] , "]" ;

object_lit      = "{" , [ key_value , { "," , key_value } ] , "}" ;
key_value       = string , ":" , expression ;
```

---

## 4. Expressions

Operator precedence from highest to lowest: primary → indexing / function call (postfix) → unary `-` → length → base expression.

```
expression      = length_expr | unary_expr ;

length_expr     = postfix_expr , "之量" ;

unary_expr      = [ "-" ] , postfix_expr ;

postfix_expr    = primary_expr , { postfix_op } ;
postfix_op      = index_suffix
                | call_suffix ;

index_suffix    = "取" , primary_expr , "之第" , primary_expr ;
call_suffix     = "施" , identifier , "於" , arg_list
                | "施" , identifier , "以虛" ;

arg_list        = expression , { "與" , expression } ;

primary_expr    = literal
                | identifier
                | "(" , expression , ")" ;
```

Notes:
- In the wenyan dialect, infix binary operators (`+ - * / % == != < <= > >=`) are **not available**. Arithmetic and comparisons use standard-library functions (`和`, `差`, `積`, `商`, `剰余` etc.) and the `若...乎、則` conditional syntax.
- Function calls use prefix notation: `施和於甲與乙` instead of `甲 + 乙`.
- Array indexing is written `取A之第i` rather than `A[i]`.
- `A之量` is the length of array or string `A`.

---

## 5. Assignment, Increment, Decrement, Append

```
assignment      = "吾有一數" , [ "、" ] , "曰" , expression ,
                  [ "、" ] , "名之曰" , identifier , "。" ;

increment       = ( "增" | "増" ) , identifier , "以一" , [ "。" ] ;
decrement       = "減" , identifier , "以一" , [ "。" ] ;

append          = "納" , expression , "入" , identifier , [ "。" ] ;
```

Note: `吾有一數、曰value、名之曰name。` assigns `value` to `name`. The value is written **before** the name (reversed from Python's `name = value`).

Note: `納x入A` appends `x` to array `A`. The value is written first.

---

## 6. Conditionals

```
if_stmt         = "若" , condition , "乎" , [ "、" ] , "則" , block ,
                  [ "否則" , block ] ,
                  "條畢" , [ "。" ] ;

condition       = expression , cmp_op , expression ;

cmp_op          = "等於"     (* == *)
                | "異於"     (* != *)
                | "小於"     (* <  *)
                | "大於"     (* >  *)
                | "不大於"   (* <= *)
                | "不小於"   (* >= *)
                | "含"       (* element of *)
                | "不含" ;   (* not element of *)
```

Comparison keyword reference:

| Wenyan keyword | Operator | Meaning                  |
|----------------|----------|--------------------------|
| `等於`         | `==`     | equal to                 |
| `異於`         | `!=`     | not equal to             |
| `小於`         | `<`      | strictly less than       |
| `大於`         | `>`      | strictly greater than    |
| `不大於`       | `<=`     | less than or equal to    |
| `不小於`       | `>=`     | greater than or equal to |
| `含`           | `∈`      | element of array/string  |
| `不含`         | `∉`      | not element of           |

---

## 7. Loops

```
repeat_stmt     = expression , "度、" , block , "度畢" , [ "。" ] ;
break_stmt      = "止" , [ "。" ] ;
```

There is no `while` loop. Simulate it with a large repeat count and `止。` (break).

---

## 8. Function Definitions and Return

```
funcdef         = "術曰" , identifier ,
                  ( funcdef_with_args | funcdef_noarg ) , block ,
                  "術畢" , [ "。" ] ;

funcdef_with_args = "以" , identifier , { "與" , identifier } ;
funcdef_noarg     = "。" ;

return_stmt     = return_value | return_none ;
return_value    = "以" , expression , "答" , [ "。" ] ;
return_none     = "還無" , [ "。" ] ;
```

If the function body ends without a `以...答。` statement, the function's local variables are implicitly returned as an object.

No-argument function syntax:
```wenyan
術曰招呼。
   以「你好！」答。
術畢。
>>> 施招呼以虛
「你好！」
```

---

## 9. Imports

```
import_stmt     = import_standard | import_named ;
import_standard = "引標準庫" ;
import_named    = "引" , identifier ;
```

---

## 10. Doctest Assertions

```
assert_stmt     = ">>>" , expression , LF , expected_value ;
expected_value  = literal ;
```

The expression after `>>>` is evaluated; its result must equal the literal on the following line.

Note: function calls in doctest lines use wenyan syntax:
```wenyan
>>> 施和於3與4
7
>>> 施招呼以虛
「你好！」
```

---

## 11. Print, Pass, and Expression Statements

```
print_stmt      = "吿曰" , expression , [ "。" ] ;
pass_stmt       = "無為" , [ "。" ] ;
expr_stmt       = expression ;
```

A standalone `expr_stmt` evaluates the expression and prints its value automatically.

---

## 12. Blocks

Blocks are delimited by structural keywords (no braces or indentation required by the parser):

| Construct      | Block opener                   | Block terminator |
|----------------|--------------------------------|------------------|
| `if_stmt`      | `若...乎、則`                  | `條畢。`         |
| `if_stmt` else | `否則`                         | `條畢。`         |
| `repeat_stmt`  | `<N>度、`                      | `度畢。`         |
| `funcdef`      | `術曰<name>以<params>` / `術曰<name>。` | `術畢。` |

```
block           = { statement } ;
```

The standard indentation is three spaces per nesting level (convention only; not enforced by the parser).

---

## 13. Standard Library Functions (Reference)

`引標準庫` must appear at the top of the program before any stdlib call.

| Function                      | Signature                            | Description                       |
|-------------------------------|--------------------------------------|-----------------------------------|
| `施和於甲與乙`                | `和(a, b, ...)` or `和([...])`       | Addition (variadic)               |
| `施差於甲與乙`                | `差(a, b)`                           | Subtraction: `a − b`              |
| `施積於甲與乙`                | `積(a, b, ...)` or `積([...])`       | Multiplication                    |
| `施商於甲與乙`                | `商(a, b)`                           | Integer/floor division            |
| `施剰余於甲與乙`              | `剰余(a, b)` (alias: `餘`)           | Modulo                            |
| `施絶対値於甲`                | `絶対値(x)`                          | Absolute value                    |
| `施平方根於甲`                | `平方根(x)`                          | Square root (returns float)       |
| `施最大値於甲與乙`            | `最大値(a, b, ...)` or `最大値([...])` | Maximum value                   |
| `施最小値於甲與乙`            | `最小値(a, b, ...)` or `最小値([...])` | Minimum value                   |
| `施乱数以虛`                  | `乱数()`                             | Random float in [0, 1)            |
| `施整数化於甲`                | `整数化(x)`                          | Convert to integer                |
| `施小数化於甲`                | `小数化(x)`                          | Convert to float                  |
| `施文字列化於甲`              | `文字列化(x)`                        | Convert to string                 |
| `施配列化於甲`                | `配列化(x)`                          | Convert string to char-code array |
| `施整数判定於甲`              | `整数判定(x)`                        | Is integer? (然/否)               |
| `施小数判定於甲`              | `小数判定(x)`                        | Is float? (然/否)                 |
| `施文字列判定於甲`            | `文字列判定(x)`                      | Is string? (然/否)                |
| `施配列判定於甲`              | `配列判定(x)`                        | Is array? (然/否)                 |
| `施オブジェクト判定於甲`      | `オブジェクト判定(x)`                | Is object? (然/否)                |
| `施真偽判定於甲`              | `真偽判定(x)`                        | Is boolean? (然/否)               |
