# Yui Language — Extended BNF Grammar Definition

This document defines the grammar of the Yui language (yui syntax dialect)
in Extended BNF.

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
                  | expr_stmt ) , LF ;
LF              = /\n/ ;
```

---

## 2. Lexical Elements

```
whitespace      = /[ \t\r　]/ ;
line_comment    = ( "#" | "＃" ) , { /[^\n]/ } ;

identifier      = simple_name | extra_name ;
simple_name     = /[A-Za-z_][A-Za-z0-9_]*/ ;
extra_name      = "「" , { /[^」]/ } , "」" ;

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

null_lit        = "値なし" ;
bool_lit        = "真" | "偽" ;

array_lit       = "[" , [ expression , { array_sep , expression } ] , "]" ;
array_sep       = "," | "、" | "，" ;

object_lit      = "{" , [ key_value , { obj_sep , key_value } ] , "}" ;
obj_sep         = "," | "、" | "，" ;
key_value       = string , ":" , expression ;
```

---

## 4. Expressions

Operator precedence from highest to lowest:
primary → indexing / function call (postfix) → unary `-` → length → base.

```
expression      = length_expr | unary_expr ;

length_expr     = postfix_expr , "の大きさ" ;

unary_expr      = [ "-" ] , postfix_expr ;

postfix_expr    = primary_expr , { postfix_op } ;
postfix_op      = index_suffix
                | call_suffix ;

index_suffix    = "[" , expression , "]" ;
call_suffix     = "(" , [ expression , { "," , expression } ] , ")" ;

primary_expr    = literal
                | identifier ;
```

Notes:
- Infix binary operators (`+ - * / % == != < <= > >=`) are **not available**.
  Arithmetic uses stdlib functions (`和/差/積/商/剰余`); comparisons use Japanese
  suffix keywords inside `もし…ならば`.
- Function calls and indexing may be chained: `f(x)[0]`, `O["a"][1]`.

---

## 5. Assignment, Increment, Decrement, Append

```
assignment      = assign_target , "=" , expression ;
assign_target   = identifier , { index_suffix } ;

increment       = assign_target , "を増やす" ;
decrement       = assign_target , "を減らす" ;

append          = append_form1 | append_form2 ;
append_form1    = assign_target , [ "の末尾" ] , "に" , expression , "を追加する" ;
append_form2    = assign_target , "を" , assign_target , "に追加する" ;
```

Notes:
- `x = expr` — standard assignment.
- `A[i] = expr` — write to index (`assign_target` includes `index_suffix`).
- `xを増やす` / `xを減らす` — increment / decrement by 1.
- `aにxを追加する` — appends `x` to array `a`.

---

## 6. Conditionals

```
if_stmt         = "もし" , condition , "ならば" , block ,
                  [ "そうでなければ" , block ] ;

condition       = expression , "が" , expression , [ cmp_suffix ] ;

cmp_suffix      = "以外"              (* != *)
                | "より小さい"         (* <  *)
                | "より大きい"         (* >  *)
                | "以下"              (* <= *)
                | "以上"              (* >= *)
                | "のいずれか"         (* in *)
                | "のいずれでもない" ;  (* not in *)
```

No `cmp_suffix` means `==` (equality).

| Keyword | Operator |
|---------|----------|
| (none) | `==` (equal) |
| `以外` | `!=` (not equal) |
| `より小さい` | `<` (less than) |
| `より大きい` | `>` (greater than) |
| `以下` | `<=` (less than or equal) |
| `以上` | `>=` (greater than or equal) |
| `のいずれか` | `∈` (element of) |
| `のいずれでもない` | `∉` (not element of) |

---

## 7. Loops

```
repeat_stmt     = expression , "回" , "くり返す" , block ;
break_stmt      = "くり返しを抜ける" ;
```

There is no `while` loop. Simulate it with a large repeat count and `くり返しを抜ける`.

---

## 8. Function Definitions and Return

```
funcdef         = identifier , "=" , func_literal ;
func_literal    = funcdef_args , "に対し" , block ;

funcdef_args    = "入力" , param_list
                | "入力なし" ;
param_list      = identifier , { "," , identifier } ;

return_stmt     = return_value | return_none ;
return_value    = expression , "が" , "答え" ;
return_none     = "関数から抜ける" ;
```

If the function body ends without `が答え` or `関数から抜ける`, the runtime returns
an object containing all local variables (implicit constructor return).

---

## 9. Import

```
import_stmt     = "標準ライブラリを使う" ;
```

---

## 10. Doctest Assertions

```
assert_stmt     = ">>>" , expression , LF , expected_value ;
expected_value  = literal ;
```

The expression after `>>>` is evaluated; its result must equal the literal.

---

## 11. Print, Pass, and Expression Statements

```
expr_stmt       = expression ;
pass_stmt       = "何もしない" ;
```

A standalone `expr_stmt` evaluates and prints its value automatically.

---

## 12. Blocks

```
block           = "{" , { statement } , "}" ;
```

Blocks are delimited by `{ … }`. Standard indentation is three spaces per nesting level.

| Construct | Opener | Terminator |
|-----------|--------|------------|
| if | `もし…ならば` | `}` |
| else | `そうでなければ` | (same `}`) |
| loop | `N回くり返す` | `}` |
| function | `NAME = 入力PARAMS に対し` | `}` |
