# Bridget Language Grammar (Extended BNF)

This document defines the grammar of the Bridget language (`bridget` syntax dialect) in extended BNF.

## Notation

- `A = B` — production rule
- `A | B` — alternation
- `[ A ]` — zero or one occurrence (optional)
- `{ A }` — zero or more repetitions
- `"..."` — terminal symbol (literal string)
- `/.../` — terminal defined by regular expression
- Whitespace (space, tab) may appear between tokens. Statements are separated by newlines.

---

## 1. Program

```
program   = { statement } ;
statement = ( import_stmt
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
LF        = /\n/ ;
```

---

## 2. Lexical Rules

```
whitespace    = /[ \t\r]/ ;
line_comment  = "#" , { /[^\n]/ } ;

identifier    = simple_name | extra_name ;
simple_name   = /[A-Za-z_][A-Za-z0-9_]*/ ;
extra_name    = "`" , { /[^`]/ } , "`" ;

integer       = /[0-9]+/ ;
float         = /[0-9]+/ , "." , /[0-9]+/ ;
number        = float | integer ;

string        = '"' , { string_part } , '"' ;
string_part   = string_char | string_escape | string_interp ;
string_char   = /[^"\\{]/ ;
string_escape = "\\" , /./ ;
string_interp = "{" , expression , "}" ;
```

---

## 3. Literals

```
literal    = null_lit | bool_lit | number | string | array_lit | object_lit ;

null_lit   = "Nothing" | "nothing" | "null" ;
bool_lit   = "Yes" | "yes" | "true" | "No" | "no" | "false" ;

array_lit  = "[" , [ expression , { "," , expression } ] , "]" ;

object_lit = "{" , [ key_value , { "," , key_value } ] , "}" ;
key_value  = string , ":" , expression ;
```

---

## 4. Expressions

Precedence (high to low): primary → length property → unary minus.

```
expression    = [ "-" ] , postfix_expr ;

postfix_expr  = primary_expr , { "'s" , "length" } ;

primary_expr  = literal
              | identifier
              | index_expr
              | funcapp_expr ;
```

### 4.1 Array Indexer

```
index_expr = "item" , expression , "in" , expression ;
```

**The index comes before the array** (`item INDEX in ARRAY`), which is the reverse of `ARRAY[INDEX]`.

```
# read
Remember that val is item i in arr

# write (as assignment target)
Remember that item i in arr is val
```

### 4.2 Length Property

```
length_expr = expression , "'s" , "length" ;
```

```
Remember that n is arr's length
When current_word's length is more than 0, then:
```

### 4.3 Function Application

```
funcapp_expr = funcname , "of" , arg_list          # one or more args
             | funcname , "," , "do" , "it" ;      # zero args
arg_list     = expression , { "and" , expression } ;
```

```
Remember that x is abs of -5
Remember that s is sum of a and b and c
Remember that r is random, do it
```

Note: binary operators (`+`, `-`, `*`, `/`, `%`) are **not used**. Use `sum`, `diff`, `product`, `quotient`, `remainder` instead.

---

## 5. Assignment / Increment / Append

```
assignment    = "Remember" , "that" , assign_target , "is" , expression ;
assign_target = identifier | index_expr ;

increment     = "Increase" , assign_target , [ "by" , "1" ] ;
decrement     = "Decrease" , assign_target , [ "by" , "1" ] ;

append        = "Add" , expression , "to" , expression ;
```

**Append argument order**: `Add ARRAY to ELEMENT` — the **array comes first**, the element to be appended comes second. This is the reverse of the natural English reading.

```
Add result to item i in string   # appends (item i in string) to result
Add current_word to char         # appends char to current_word
```

---

## 6. Conditional

```
if_stmt    = "When" , condition , "," , "then" , ":" , block ,
             [ "But" , "," , "if" , "not" , ":" , block ] ,
             "End" , "when" ;

condition  = expression , comparator , expression ;
```

### Comparison Operators

| Bridget phrase | Mathematical meaning | Note |
|----------------|----------------------|------|
| `is` | `==` | |
| `is not` | `!=` | |
| `is less than` | `<` | |
| `is more than` | `>` | |
| `is at least` | `<=` | ⚠ opposite of everyday English |
| `is at most` | `>=` | ⚠ opposite of everyday English |
| `is in` | `in` | |
| `is not in` | `not in` | |

`is at least` and `is at most` are **counterintuitive**: in everyday English "at least" implies ≥, but in Bridget it means ≤, and vice versa.

```
When i is at least m, then:     # if i <= m  (NOT i >= m)
   ...
End when
When count is at most 0, then:  # if count >= 0  (NOT count <= 0)
   ...
End when
```

---

## 7. Repeat

```
repeat_stmt = "Do" , "this" , expression , "times" , ":" , block , "End" , "do" ;
break_stmt  = "Leave" , "the" , "loop" ;
```

```
Do this length times:
   Remember that val is item i in arr
   Increase i
End do
```

---

## 8. Function Definition and Return

```
funcdef     = "This" , "is" , "how" , "to" , funcname ,
              "of" , param_list , ":" , block ,
              "Now" , "you" , "know" ;
param_list  = identifier , { "and" , identifier } ;

return_stmt = "The" , "answer" , "is" , expression ;
return_none = "Stop" , "here" ;
```

```
This is how to add of x and y:
   Remember that result is sum of x and y
   The answer is result
Now you know
```

---

## 9. Import

```
import_stmt = "Use" , "the" , "standard" , "library" ;
```

---

## 10. Doctest (Assert)

```
assert_stmt    = ">>>" , expression , LF , expected_value ;
expected_value = literal ;
```

`>>>` followed by an expression is evaluated and compared against the value on the next line.

---

## 11. Other Statements

```
pass_stmt  = "Do" , "nothing" ;
print_stmt = "Now" , "," , expression ;
expr_stmt  = expression ;
```

---

## 12. Block

```
block = { statement } ;
```

Blocks are delimited by indentation (2 spaces per level).
Closing keywords (`End when`, `End do`, `Now you know`) mark the end of each construct.
