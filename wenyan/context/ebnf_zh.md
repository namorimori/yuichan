# Wenyan Language — Extended BNF Grammar Definition

This document defines the grammar of the Yui language using the **wenyan**
(Classical Chinese) syntax dialect in Extended BNF.

## Notation

- `A = B` — production rule
- `A | B` — alternation
- `[ A ]` — zero or one occurrence (optional)
- `{ A }` — zero or more repetitions
- `"..."` — terminal symbol (literal string)
- `/.../` — terminal defined by regular expression
- Whitespace (space, tab, fullwidth space) may appear between lexical elements.
  Statements are separated by newline `LF`.

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

null_lit        = "無" ;
bool_lit        = "然" | "否" ;

array_lit       = "[" , [ expression , { "," , expression } ] , "]" ;

object_lit      = "{" , [ key_value , { "," , key_value } ] , "}" ;
key_value       = string , ":" , expression ;
```

---

## 4. Expressions

Operator precedence from highest to lowest:
primary → indexing / function call (postfix) → unary `-` → length → base.

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
- Infix binary operators (`+ - * / % == != < <= > >=`) are **not available**.
  Arithmetic uses stdlib functions via `施func於args`; comparisons use Chinese
  keywords inside `若…乎、則`.
- Array indexing is `取A之第i` rather than `A[i]`.
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

Notes:
- `吾有一數、曰VALUE、名之曰NAME。` — value comes **before** name.
- `identifier` in assignment may be an index expression (`取A之第i`),
  which writes to that position.
- `增取甲之第0以一。` increments an indexed element (`甲[0] += 1`).
- `納x入A。` appends `x` to array `A`.

---

## 6. Conditionals

```
if_stmt         = "若" , condition , "乎" , [ "、" ] , "則" , block ,
                  [ "否則" , block ] ,
                  "條畢" , [ "。" ] ;

condition       = expression , cmp_op , expression ;

cmp_op          = "等於"    (* == *)
                | "異於"    (* != *)
                | "小於"    (* <  *)
                | "大於"    (* >  *)
                | "不大於"  (* <= *)
                | "不小於"  (* >= *)
                | "含"      (* element of *)
                | "不含" ;  (* not element of *)
```

`cmp_op` meanings:

| Keyword | Operator |
|---------|----------|
| `等於` | `==` (equal to) |
| `異於` | `!=` (not equal to) |
| `小於` | `<` (strictly less than) |
| `大於` | `>` (strictly greater than) |
| `不大於` | `<=` (less than or equal to) |
| `不小於` | `>=` (greater than or equal to) |
| `含` | `∈` (element of array/string) |
| `不含` | `∉` (not element of) |

---

## 7. Loops

```
repeat_stmt     = expression , "度" , [ "、" ] , block , "度畢" , [ "。" ] ;
break_stmt      = "止" , [ "。" ] ;
```

There is no `while` loop. Simulate it with a large repeat count and `止。`.

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

If the function body ends without `以...答。` or `還無。`, the runtime returns
an object containing all local variables (implicit constructor return).

---

## 9. Import

```
import_stmt     = "引標準庫" ;
```

---

## 10. Doctest Assertions

```
assert_stmt     = ">>>" , expression , LF , expected_value ;
expected_value  = literal ;
```

The expression after `>>>` is evaluated; its result must equal the literal.

```wenyan
>>> 施後繼於0
1
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

A standalone `expr_stmt` evaluates and prints its value automatically.

---

## 12. Blocks

```
block           = { statement } ;
```

Blocks are delimited by structural keywords (no braces or indentation required).
Standard indentation is three spaces per nesting level (convention only).

| Construct | Opener | Terminator |
|-----------|--------|------------|
| if | `若…乎、則` | `條畢。` |
| else | `否則` | (same `條畢。`) |
| loop | `N度、` | `度畢。` |
| function (with args) | `術曰NAME以PARAMS` | `術畢。` |
| function (no args) | `術曰NAME。` | `術畢。` |
