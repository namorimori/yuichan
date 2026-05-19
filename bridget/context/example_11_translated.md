```bridget
Use the standard library
# Simple stack machine
# Instructions are [opcode, operand] arrays. Set operand to 0 when unused.
#
# Supported instructions:
#   ["PUSH", n] -- push n onto the stack
#   ["POP",  0] -- discard the top
#   ["DUP",  0] -- duplicate the top
#   ["ADD",  0] -- pop two values, push a+b
#   ["SUB",  0] -- pop two values, push a-b
#   ["MUL",  0] -- pop two values, push a*b
#
# Returns the top of the stack after execution.
# (Bridget arrays have no removal; logical size is tracked via top,
#  and POP simply decrements top)

This is how to run of program:
   Remember that stack is []
   Remember that top is 0
   Remember that n is program's length
   Remember that i is 0
   Do this n times:
      Remember that instr is item i in program
      Remember that op is item 0 in instr
      Remember that arg is item 1 in instr
      When op is "PUSH", then:
         Remember that sz is stack's length
         When top is less than sz, then:
            Remember that item top in stack is arg
         But, if not:
            Add stack to arg
         End when
         Increase top
      End when
      When op is "POP", then:
         Decrease top
      End when
      When op is "DUP", then:
         Remember that t is diff of top and 1
         Remember that x is item t in stack
         Remember that sz is stack's length
         When top is less than sz, then:
            Remember that item top in stack is x
         But, if not:
            Add stack to x
         End when
         Increase top
      End when
      When op is "ADD", then:
         Decrease top
         Remember that b is item top in stack
         Decrease top
         Remember that a is item top in stack
         Remember that item top in stack is sum of a and b
         Increase top
      End when
      When op is "SUB", then:
         Decrease top
         Remember that b is item top in stack
         Decrease top
         Remember that a is item top in stack
         Remember that item top in stack is diff of a and b
         Increase top
      End when
      When op is "MUL", then:
         Decrease top
         Remember that b is item top in stack
         Decrease top
         Remember that a is item top in stack
         Remember that item top in stack is product of a and b
         Increase top
      End when
      Increase i
   End do
   Decrease top
   The answer is item top in stack
Now you know

# Test: 3 + 4 = 7
>>> run of [["PUSH", 3], ["PUSH", 4], ["ADD", 0]]
7
# Test: (3 + 4) * 2 = 14
>>> run of [["PUSH", 3], ["PUSH", 4], ["ADD", 0], ["PUSH", 2], ["MUL", 0]]
14
# Test: 10 - (2 + 3) = 5
>>> run of [["PUSH", 10], ["PUSH", 2], ["PUSH", 3], ["ADD", 0], ["SUB", 0]]
5
# Test: DUP 5 then multiply → 25
>>> run of [["PUSH", 5], ["DUP", 0], ["MUL", 0]]
25
# Test: POP discards the top → 7
>>> run of [["PUSH", 7], ["PUSH", 99], ["POP", 0]]
7
# Test: single PUSH
>>> run of [["PUSH", 42]]
42
```

```bridget
# Grade A/B/C/D/F from score
# Bridget has no elif; chain branches by nesting When inside But, if not.
# A: >= 90, B: >= 80, C: >= 70, D: >= 60, F: below 60
# Note: "is at most N" means >= N in Bridget (counterintuitive).

This is how to grade of score:
   Remember that result is "F"
   When score is at most 90, then:
      Remember that result is "A"
   But, if not:
      When score is at most 80, then:
         Remember that result is "B"
      But, if not:
         When score is at most 70, then:
            Remember that result is "C"
         But, if not:
            When score is at most 60, then:
               Remember that result is "D"
            End when
         End when
      End when
   End when
   The answer is result
Now you know

>>> grade of 100
"A"
>>> grade of 95
"A"
>>> grade of 89
"B"
>>> grade of 70
"C"
>>> grade of 65
"D"
>>> grade of 59
"F"
>>> grade of 0
"F"

# Pass/fail: anything other than F passes
This is how to passed of score:
   Remember that g is grade of score
   When g is not "F", then:
      The answer is Yes
   But, if not:
      The answer is No
   End when
Now you know

>>> passed of 75
Yes
>>> passed of 40
No
```

```bridget
Use the standard library
# Three ways to return multiple values from a function
#
#   1. Return an array:   [a, b]              access with item 0 in r, item 1 in r
#   2. Return an object:  {"q": ..., "r": …}  access with item "q" in r
#   3. Implicit return:   omit The answer is  — all locals bundled as an object
#                         (useful as a constructor pattern)

# === 1. Array return: quotient and remainder together ===
This is how to divmod_array of a and b:
   Remember that q is quotient of a and b
   Remember that r is remainder of a and b
   The answer is [q, r]
Now you know

# === 2. Object return: array statistics ===
This is how to stats of arr:
   Remember that lo is item 0 in arr
   Remember that hi is item 0 in arr
   Remember that total is 0
   Remember that n is arr's length
   Remember that i is 0
   Do this n times:
      Remember that x is item i in arr
      When x is less than lo, then:
         Remember that lo is x
      End when
      When x is more than hi, then:
         Remember that hi is x
      End when
      Remember that total is sum of total and x
      Increase i
   End do
   The answer is {"min": lo, "max": hi, "sum": total, "count": n}
Now you know

# === 3. Implicit return: constructor pattern ===
# Omitting The answer is returns all locals as an object — handy for small structs.
This is how to point of x and y:
   # No explicit return → returns {"x": x, "y": y}
Now you know

# === Tests 1: array return ===
>>> divmod_array of 17 and 5
[3, 2]
>>> divmod_array of 20 and 4
[5, 0]
# Extract individual elements
Remember that qr is divmod_array of 17 and 5
>>> item 0 in qr
3
>>> item 1 in qr
2

# === Tests 2: object return ===
Remember that s is stats of [3, 1, 4, 1, 5, 9, 2, 6]
>>> item "min" in s
1
>>> item "max" in s
9
>>> item "sum" in s
31
>>> item "count" in s
8

# === Tests 3: implicit return ===
Remember that P is point of 3 and 5
>>> item "x" in P
3
>>> item "y" in P
5
```

```bridget
Use the standard library
# Compound interest
#
# Final amount after n years at annual rate r on principal P:
#   A = P * (1 + r)^n
# Bridget has no exponentiation, so we multiply by (1 + r) in a loop.
#
# Rate r is a decimal (e.g. 5% → 0.05). Result is a float.

# === 1. Balance after n years ===
This is how to compound of P and r and n:
   Remember that balance is tofloat of P
   Remember that factor is sum of (tofloat of 1) and r
   Do this n times:
      Remember that balance is product of balance and factor
   End do
   The answer is balance
Now you know

# === 2. Years to double (whole-year ceiling) ===
# Returns the first year when balance >= 2x the original principal
This is how to years_to_double of r:
   Remember that balance is tofloat of 1
   Remember that factor is sum of (tofloat of 1) and r
   Remember that n is 0
   Do this 1000 times:
      When balance is at most 2, then:
         Leave the loop
      End when
      Remember that balance is product of balance and factor
      Increase n
   End do
   The answer is n
Now you know

# === Tests: year 1 ===
>>> compound of 1000 and 0.05 and 1
1050.000000
# === Tests: year 2 (1000 × 1.05²) ===
>>> compound of 1000 and 0.05 and 2
1102.500000
# === Tests: year 3 (1000 × 1.10³) ===
>>> compound of 1000 and 0.10 and 3
1331.000000
# === Tests: rate 0 → principal unchanged ===
>>> compound of 100 and 0.0 and 5
100.000000
# === Tests: 0 years → principal unchanged ===
>>> compound of 1000 and 0.05 and 0
1000.000000

# === Tests: 10% annual → doubles in 8 years ===
>>> years_to_double of 0.10
8
# === Tests: 7% → 11 years ===
>>> years_to_double of 0.07
11
# === Tests: 5% → 15 years (Rule of 72) ===
>>> years_to_double of 0.05
15
```

```bridget
# String interpolation, no-arg function (^^), tostring

# No-arg function: returns a constant
This is how to motto ^^:
   The answer is "Keep going!"
Now you know

>>> motto, do it
"Keep going!"

# String interpolation: embed {expr} anywhere in a string
This is how to greet of name:
   The answer is "Hello, {name}!"
Now you know

>>> greet of "Yui"
"Hello, Yui!"

# Multiple interpolated values
This is how to score_msg of name and points:
   The answer is "{name}'s score is {points} points"
Now you know

>>> score_msg of "Taro" and 95
"Taro's score is 95 points"

# tostring: pure number-to-string conversion
>>> tostring of 42
"42"
```

```bridget
# Membership testing with is in / is not in

Remember that menu is ["curry", "ramen", "sushi", "soba"]

# is in: check if an element is in a collection
This is how to check of val:
   When val is in menu, then:
      The answer is "available"
   But, if not:
      The answer is "not available"
   End when
Now you know

>>> check of "sushi"
"available"
>>> check of "pizza"
"not available"

# is not in: direct absence check (e.g. allergy filter)
Remember that allergy is ["egg", "soba", "wheat"]

This is how to safe of food:
   When food is not in allergy, then:
      The answer is Yes
   But, if not:
      The answer is No
   End when
Now you know

>>> safe of "curry"
Yes
>>> safe of "soba"
No
>>> safe of "egg"
No
```

```bridget
# Do nothing demo
# Use it when a branch deliberately takes no action,
# or as a placeholder where a statement is syntactically required.

This is how to sign of n:
   Remember that result is ""
   When n is 0, then:
      Do nothing
   But, if not:
      When n is less than 0, then:
         Remember that result is "negative"
      But, if not:
         Remember that result is "positive"
      End when
   End when
   The answer is result
Now you know

>>> sign of 5
"positive"
>>> sign of -3
"negative"
>>> sign of 0
""
```

```bridget
Use the standard library
# Roll a die N times and count occurrences of each face (1–6)
# random, do it returns a float in [0, 1);
# multiply by 6 and truncate → integer in 0..5

This is how to count_dice of N:
   # counts[i] holds the number of times face (i+1) appeared
   Remember that counts is [0, 0, 0, 0, 0, 0]
   Do this N times:
      Remember that r is toint of (product of (random, do it) and 6)
      Increase item r in counts
   End do
   The answer is counts
Now you know

# Live runs (content is random)
count_dice of 60
count_dice of 600

# Test: N=0 → all zeros
>>> count_dice of 0
[0, 0, 0, 0, 0, 0]
# Test: total count equals N
>>> sum of (count_dice of 60)
60
>>> sum of (count_dice of 1000)
1000
```

```bridget
Use the standard library
# ROT13: rotate each letter 13 places — the classic self-inverse cipher
# Strings are stored as character-code arrays, so we access them one code at a time.
# Char codes: 'A'=65  'Z'=90  'a'=97  'z'=122
# ROT13 is its own inverse: applying it twice restores the original.
# Note: "is at most N" means >= N; "is at least N" means <= N (Bridget convention).

This is how to rot13 of s:
   Remember that result is ""
   Remember that n is s's length
   Remember that i is 0
   Do this n times:
      Remember that c is item i in s
      Remember that nc is c
      # Uppercase A..Z  (65 <= c <= 90)
      When c is at most 65, then:
         When c is at least 90, then:
            Remember that offset is diff of c and 65
            Remember that shifted is remainder of (sum of offset and 13) and 26
            Remember that nc is sum of shifted and 65
         End when
      End when
      # Lowercase a..z  (97 <= c <= 122)
      When c is at most 97, then:
         When c is at least 122, then:
            Remember that offset is diff of c and 97
            Remember that shifted is remainder of (sum of offset and 13) and 26
            Remember that nc is sum of shifted and 97
         End when
      End when
      Add result to nc
      Increase i
   End do
   The answer is result
Now you know

# Test: uppercase basic  ABC → NOP
>>> rot13 of "ABC"
"NOP"
# Test: lowercase with wrap  xyz → klm
>>> rot13 of "xyz"
"klm"
# Test: mixed + symbols + digits (non-alpha unchanged)
>>> rot13 of "Hello, World!"
"Uryyb, Jbeyq!"
# Test: self-inverse
>>> rot13 of "Uryyb, Jbeyq!"
"Hello, World!"
# Test: digits and symbols unchanged
>>> rot13 of "123 !?"
"123 !?"
# Test: empty string
>>> rot13 of ""
""
```

```bridget
Use the standard library
# Six type-check functions and Nothing (null)

# Integer check
>>> isint of 42
Yes
>>> isint of 3.14
No

# Float check
>>> isfloat of 3.14
Yes
>>> isfloat of 42
No

# String check
>>> isstring of "hello"
Yes
>>> isstring of 42
No

# Array check
>>> isarray of [1, 2, 3]
Yes

# Object check
>>> isobject of {"x": 1}
Yes
>>> isobject of [1, 2, 3]
No

# Boolean check
>>> isbool of Yes
Yes
>>> isbool of 1
No

# Nothing (null) matches none of the type checks
Remember that x is Nothing
>>> isint of x
No
>>> isstring of x
No
>>> isarray of x
No
```

```bridget
# Backtick identifier (extra_name) and Stop here demo
#
# Wrap any phrase (spaces, hyphens, etc.) in backticks to use it as an identifier.
# Here we use backtick names for both a variable and a function.

# Backtick identifier as a variable
Remember that `passing score` is 60

# Backtick identifier as a function name
# Stop here: return Nothing early (early exit without a value)
This is how to `is passing score` of score:
   When score is less than `passing score`, then:
      Stop here
   End when
   The answer is Yes
Now you know

# Collect names of students who passed
# Add ARRAY to ELEMENT: array comes first, new element second
This is how to `collect passers` of scores and names:
   Remember that passers is []
   Remember that n is scores's length
   Remember that i is 0
   Do this n times:
      Remember that r is `is passing score` of (item i in scores)
      When r is Yes, then:
         Add passers to (item i in names)
      End when
      Increase i
   End do
   The answer is passers
Now you know

# Tests: backtick identifier and Stop here
>>> `is passing score` of 75
Yes
>>> `is passing score` of 60
Yes
>>> `is passing score` of 59
Nothing

# Tests: Add ARRAY to ELEMENT and backtick function name
>>> `collect passers` of [85, 55, 72, 40, 90] and ["Alice", "Bob", "Carol", "Dave", "Eve"]
["Alice", "Carol", "Eve"]
>>> `collect passers` of [100, 0] and ["top", "zero"]
["top"]
>>> `collect passers` of [10, 20] and ["A", "B"]
[]
```
