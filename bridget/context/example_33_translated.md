```bridget
Use the standard library
# Convert a binary string to an integer
# Example: "1011" → 11  (1*8 + 0*4 + 1*2 + 1*1)
#
# Algorithm: read left to right, double result and add the new bit.
#   "1011" step by step: 0 → 1 → 2 → 5 → 11
#
# Strings are stored as char-code arrays. '0' = 48, '1' = 49,
# so subtract 48 from each code to get the bit value.

This is how to bin_to_int of s:
   Remember that result is 0
   Remember that n is s's length
   Remember that i is 0
   Do this n times:
      Remember that c is item i in s
      Remember that bit is diff of c and 48
      Remember that result is sum of (product of result and 2) and bit
      Increase i
   End do
   The answer is result
Now you know

# Test: single digit
>>> bin_to_int of "0"
0
>>> bin_to_int of "1"
1
# Test: basic conversions
>>> bin_to_int of "10"
2
>>> bin_to_int of "11"
3
>>> bin_to_int of "1011"
11
# Test: 8-bit maximum
>>> bin_to_int of "11111111"
255
# Test: 9-bit
>>> bin_to_int of "100000000"
256
# Test: leading zeros ignored
>>> bin_to_int of "0001010"
10
# Test: empty string → 0
>>> bin_to_int of ""
0
```

```bridget
# Bit addition: full adder with carry, repeated for each bit position.
# In Bridget, integers are stored as bit arrays (LSB first):
#   6 = 0b110 → [0, 1, 1]  (item 0 in 6 = 0, item 1 in 6 = 1, 6's length = 3)
#
# For each position: s = a_bit + b_bit + carry  (0..3)
#   s=0: x=0 c=0    s=1: x=1 c=0
#   s=2: x=0 c=1    s=3: x=1 c=1
# Scan max+1 positions to handle overflow carry.

This is how to bits_add of A and B:
   Remember that maxlen is A's length
   When B's length is more than maxlen, then:
      Remember that maxlen is B's length
   End when
   Increase maxlen
   Remember that c is 0
   Remember that X is 0
   Remember that index is 0
   Do this maxlen times:
      Remember that a is 0
      When index is less than A's length, then:
         Remember that a is item index in A
      End when
      Remember that b is 0
      When index is less than B's length, then:
         Remember that b is item index in B
      End when
      Remember that s is 0
      When a is 1, then:
         Increase s
      End when
      When b is 1, then:
         Increase s
      End when
      When c is 1, then:
         Increase s
      End when
      Remember that x is 0
      Remember that c is 0
      When s is 1, then:
         Remember that x is 1
      End when
      When s is 2, then:
         Remember that c is 1
      End when
      When s is 3, then:
         Remember that x is 1
         Remember that c is 1
      End when
      Add X to x
      Increase index
   End do
   The answer is X
Now you know

>>> bits_add of 3 and 5
8
>>> bits_add of 1 and 1
2
>>> bits_add of 15 and 1
16
```

```bridget
Use the standard library
# Bitwise AND, OR, XOR — standard library functions
# In Bridget, integers are stored as bit arrays (LSB first):
#   6 = 0b110 → [0, 1, 1],  5 = 0b101 → [1, 0, 1]

# Bitwise AND: 1 only when both bits are 1
>>> bitand of 6 and 5
4
>>> bitand of 3 and 1
1
>>> bitand of 6 and 0
0

# Bitwise OR: 1 when either bit is 1
>>> bitor of 6 and 5
7
>>> bitor of 4 and 3
7
>>> bitor of 0 and 5
5

# Bitwise XOR: 1 when exactly one bit is 1
>>> bitxor of 6 and 5
3
>>> bitxor of 3 and 3
0
>>> bitxor of 0 and 7
7
```

```bridget
Use the standard library
# Bit shifting — standard library functions
# lshift of n and k  →  n * 2^k
# rshift of n and k  →  n // 2^k  (floor division)

# Left shift
>>> lshift of 1 and 3
8
>>> lshift of 3 and 2
12
>>> lshift of 5 and 1
10
# Zero shift is identity
>>> lshift of 7 and 0
7
>>> rshift of 7 and 0
7
# Right shift (floor division)
>>> rshift of 8 and 3
1
>>> rshift of 12 and 2
3
# Fractional part is truncated
>>> rshift of 13 and 2
3
# Large shift gives 0
>>> rshift of 5 and 3
0
# Shifting 0 stays 0
>>> lshift of 0 and 5
0
>>> rshift of 0 and 5
0
# Left then right restores value (no fractional loss in this range)
>>> rshift of (lshift of 11 and 4) and 4
11
```

```bridget
Use the standard library
# BMI (Body Mass Index) classification
# BMI = weight(kg) / height(m)^2. WHO categories:
#   BMI < 18.5  → "underweight"
#   BMI < 25    → "normal"
#   BMI < 30    → "overweight"
#   otherwise   → "obese"
# Early-return pattern: thresholds in ascending order.

This is how to bmi_category of w and h:
   Remember that weight is tofloat of w
   Remember that h2 is product of h and h
   Remember that bmi is quotient of weight and h2
   When bmi is less than 18.5, then:
      The answer is "underweight"
   End when
   When bmi is less than 25, then:
      The answer is "normal"
   End when
   When bmi is less than 30, then:
      The answer is "overweight"
   End when
   The answer is "obese"
Now you know

# Test: underweight (1.70m, 50kg → BMI ≈ 17.3)
>>> bmi_category of 50 and 1.70
"underweight"
# Test: normal (1.70m, 65kg → BMI ≈ 22.5)
>>> bmi_category of 65 and 1.70
"normal"
# Test: overweight (1.70m, 80kg → BMI ≈ 27.7)
>>> bmi_category of 80 and 1.70
"overweight"
# Test: obese (1.70m, 100kg → BMI ≈ 34.6)
>>> bmi_category of 100 and 1.70
"obese"
# Test: other heights
>>> bmi_category of 55 and 1.60
"normal"
>>> bmi_category of 90 and 1.65
"obese"
# Test: borderline underweight
>>> bmi_category of 45 and 1.70
"underweight"
```

```bridget
Use the standard library
# Bubble sort: compare adjacent elements and move larger ones toward the end

This is how to bubble_sort of A:
   Remember that n is A's length
   Do this n times:
      Remember that i is 0
      Do this (diff of n and 1) times:
         Remember that j is sum of i and 1
         When item i in A is more than item j in A, then:
            Remember that tmp is item i in A
            Remember that item i in A is item j in A
            Remember that item j in A is tmp
         End when
         Increase i
      End do
   End do
   The answer is A
Now you know

# Test: unsorted array
>>> bubble_sort of [3,1,4,1,5,9,2,6]
[1, 1, 2, 3, 4, 5, 6, 9]
# Test: reverse order
>>> bubble_sort of [5,4,3,2,1]
[1, 2, 3, 4, 5]
# Test: already sorted
>>> bubble_sort of [1,2,3]
[1, 2, 3]
# Test: single element
>>> bubble_sort of [42]
[42]
# Test: empty array
>>> bubble_sort of []
[]
```

```bridget
Use the standard library
# Find the element in arr closest to target (by |x - target|)
# If two elements are equally close, return the first one.

This is how to closest of arr and target:
   Remember that n is arr's length
   Remember that best is item 0 in arr
   Remember that bestd is abs of (diff of best and target)
   Remember that i is 1
   Do this (diff of n and 1) times:
      Remember that x is item i in arr
      Remember that d is abs of (diff of x and target)
      When d is less than bestd, then:
         Remember that best is x
         Remember that bestd is d
      End when
      Increase i
   End do
   The answer is best
Now you know

# Test: closest to 10
>>> closest of [1,5,9,12,20] and 10
9
# Test: 12 is closer to 11
>>> closest of [1,5,9,12,20] and 11
12
# Test: 5 is closer to 6
>>> closest of [1,5,9,12,20] and 6
5
# Test: single element
>>> closest of [42] and 100
42
# Test: negative values
>>> closest of [-5,-2,3,8] and 0
-2
# Test: target in array
>>> closest of [1,2,3,4,5] and 3
3
# Test: tie goes to first (1 and 3 are both distance 1 from 2)
>>> closest of [1,3] and 2
1
```

```bridget
Use the standard library
# Compound interest
# Final amount after n years at annual rate r on principal P: A = P * (1+r)^n
# No exponentiation — multiply by (1+r) in a loop.
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
# Returns first year when balance >= 2x the original principal.
# Note: "is at most 2" means >= 2 in Bridget.
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

# Test: year 1
>>> compound of 1000 and 0.05 and 1
1050.000000
# Test: year 2 (1000 × 1.05²)
>>> compound of 1000 and 0.05 and 2
1102.500000
# Test: year 3 (1000 × 1.10³)
>>> compound of 1000 and 0.10 and 3
1331.000000
# Test: rate 0 → principal unchanged
>>> compound of 100 and 0.0 and 5
100.000000
# Test: 0 years → principal unchanged
>>> compound of 1000 and 0.05 and 0
1000.000000

# Test: 10% annual → doubles in 8 years
>>> years_to_double of 0.10
8
# Test: 7% → 11 years
>>> years_to_double of 0.07
11
# Test: 5% → 15 years (Rule of 72)
>>> years_to_double of 0.05
15
```

```bridget
Use the standard library
# Count vowels / find first vowel (break on first match)
# Strings are stored as char-code arrays, so "is in" works for membership.

# Count all vowels in string s
This is how to count_vowels of s:
   Remember that vowels is "aeiouAEIOU"
   Remember that count is 0
   Remember that i is 0
   Do this s's length times:
      Remember that c is item i in s
      When c is in vowels, then:
         Increase count
      End when
      Increase i
   End do
   The answer is count
Now you know

>>> count_vowels of "hello"
2
>>> count_vowels of "programming"
3
>>> count_vowels of "xyz"
0
>>> count_vowels of "AEIOU"
5

# Find the first vowel; return "" if none found
This is how to first_vowel of s:
   Remember that vowels is "aeiouAEIOU"
   Remember that result is ""
   Remember that i is 0
   Do this s's length times:
      Remember that c is item i in s
      When c is in vowels, then:
         Add result to c
         Leave the loop
      End when
      Increase i
   End do
   The answer is result
Now you know

>>> first_vowel of "hello"
"e"
>>> first_vowel of "sky"
""
>>> first_vowel of "Apple"
"A"
```

```bridget
Use the standard library
# Roll a die N times and count occurrences of each face (1–6)
# random, do it returns a float in [0, 1);
# multiply by 6 and truncate → integer in 0..5

This is how to count_dice of N:
   Remember that counts is [0, 0, 0, 0, 0, 0]
   Do this N times:
      Remember that r is toint of (product of (random, do it) and 6)
      Increase item r in counts
   End do
   The answer is counts
Now you know

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
# Euclidean distance d = sqrt((x2-x1)^2 + (y2-y1)^2)

This is how to distance of x1 and y1 and x2 and y2:
   Remember that dx is diff of x2 and x1
   Remember that dy is diff of y2 and y1
   Remember that d2 is sum of (product of dx and dx) and (product of dy and dy)
   The answer is sqrt of d2
Now you know

# Test: 3-4-5 right triangle
>>> distance of 0 and 0 and 3 and 4
5.000000
# Test: same point → 0
>>> distance of 7 and 7 and 7 and 7
0.000000
# Test: negative coordinates (-1,0)→(2,4): diff is (3,4)
>>> distance of -1 and 0 and 2 and 4
5.000000
# Test: 5-12-13
>>> distance of 0 and 0 and 5 and 12
13.000000
```

```bridget
Use the standard library
# Dot product of two equal-length vectors: Σ a[i] * b[i]

This is how to dot of a and b:
   Remember that total is 0
   Remember that n is a's length
   Remember that i is 0
   Do this n times:
      Remember that total is sum of total and (product of (item i in a) and (item i in b))
      Increase i
   End do
   The answer is total
Now you know

# Test: 1*4 + 2*5 + 3*6 = 32
>>> dot of [1,2,3] and [4,5,6]
32
# Test: orthogonal vectors → 0
>>> dot of [1,0,0] and [0,1,0]
0
# Test: self dot product = sum of squares: 2*2+3*3 = 13
>>> dot of [2,3] and [2,3]
13
# Test: dot with all-ones = sum of elements
>>> dot of [1,2,3,4] and [1,1,1,1]
10
# Test: empty vectors
>>> dot of [] and []
0
# Test: negative values: 2*(-1) + (-3)*4 = -14
>>> dot of [2,-3] and [-1,4]
-14
```

```bridget
Use the standard library
# Grade A/B/C/D/F from score
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
Use the standard library
# Leap year test (Gregorian calendar):
#   Divisible by 400 → leap year
#   Divisible by 100 (not 400) → not leap year
#   Divisible by 4   (not 100) → leap year
#   Otherwise → not leap year
# Early-return pattern: strongest condition first.

This is how to leap_year of y:
   Remember that r400 is remainder of y and 400
   When r400 is 0, then:
      The answer is Yes
   End when
   Remember that r100 is remainder of y and 100
   When r100 is 0, then:
      The answer is No
   End when
   Remember that r4 is remainder of y and 4
   When r4 is 0, then:
      The answer is Yes
   End when
   The answer is No
Now you know

# Test: divisible by 400 → leap
>>> leap_year of 2000
Yes
>>> leap_year of 1600
Yes
# Test: divisible by 100 but not 400 → not leap
>>> leap_year of 1900
No
>>> leap_year of 2100
No
>>> leap_year of 1700
No
# Test: divisible by 4 but not 100 → leap
>>> leap_year of 2024
Yes
>>> leap_year of 2020
Yes
>>> leap_year of 1996
Yes
# Test: not divisible by 4 → not leap
>>> leap_year of 2023
No
>>> leap_year of 2025
No
>>> leap_year of 2001
No
```

```bridget
Use the standard library
# Leibniz formula for π approximation:
#   π / 4 ≈ 1 − 1/3 + 1/5 − 1/7 + ...
# Returns 4 × (sum of first N terms).

This is how to leibniz of N:
   Remember that total is tofloat of 0
   Remember that k is 0
   Do this N times:
      Remember that denom is tofloat of (sum of (product of 2 and k) and 1)
      Remember that term is quotient of (tofloat of 1) and denom
      Remember that parity is remainder of k and 2
      When parity is 0, then:
         Remember that total is sum of total and term
      But, if not:
         Remember that total is diff of total and term
      End when
      Increase k
   End do
   The answer is product of (tofloat of 4) and total
Now you know

# Test: first term only (4 × 1)
>>> leibniz of 1
4.000000
# Test: first 2 terms (4 × (1 − 1/3))
>>> leibniz of 2
2.666667
# Test: first 4 terms
>>> leibniz of 4
2.895238
# Test: first 100 terms
>>> leibniz of 100
3.131593
# Test: first 1000 terms (matches π to 2 decimal places)
>>> leibniz of 1000
3.140593
```

```bridget
Use the standard library
# NxN matrix determinant via Laplace expansion
# Matrix is an array of arrays: [[1,2],[3,4]] is a 2x2 matrix

# Submatrix: remove row r and column c
This is how to minor of M and r and c:
   Remember that result is []
   Remember that n is M's length
   Remember that i is 0
   Do this n times:
      When i is not r, then:
         Remember that row is []
         Remember that j is 0
         Do this n times:
            When j is not c, then:
               Add row to (item j in (item i in M))
            End when
            Increase j
         End do
         Add result to row
      End when
      Increase i
   End do
   The answer is result
Now you know

# Determinant via Laplace expansion along row 0
# det(M) = Σ_j (-1)^j * M[0][j] * det(minor(M, 0, j))
This is how to det of M:
   Remember that n is M's length
   When n is 1, then:
      The answer is item 0 in (item 0 in M)
   End when
   Remember that total is 0
   Remember that j is 0
   Do this n times:
      Remember that cof is product of (item j in (item 0 in M)) and (det of (minor of M and 0 and j))
      Remember that parity is remainder of j and 2
      When parity is 0, then:
         Remember that total is sum of total and cof
      But, if not:
         Remember that total is diff of total and cof
      End when
      Increase j
   End do
   The answer is total
Now you know

# Test: 1x1
>>> det of [[5]]
5
>>> det of [[-3]]
-3
# Test: 2x2  |1 2; 3 4| = 1*4 - 2*3 = -2
>>> det of [[1,2],[3,4]]
-2
# Test: 2x2 identity
>>> det of [[1,0],[0,1]]
1
# Test: 3x3  |1 2 3; 4 5 6; 7 8 10| = -3
>>> det of [[1,2,3],[4,5,6],[7,8,10]]
-3
# Test: 3x3 identity
>>> det of [[1,0,0],[0,1,0],[0,0,1]]
1
# Test: 4x4 diagonal diag(1,2,3,4) = 24
>>> det of [[1,0,0,0],[0,2,0,0],[0,0,3,0],[0,0,0,4]]
24
# Test: linearly dependent rows → 0
>>> det of [[1,2,3],[2,4,6],[7,8,9]]
0
```

```bridget
Use the standard library
# max, min, abs — standard library functions

# Variable arguments
>>> max of 3 and 1 and 4 and 1 and 5 and 9 and 2 and 6
9
>>> min of 3 and 1 and 4 and 1 and 5 and 9 and 2 and 6
1

# Can also pass an array
Remember that scores is [72,85,90,68,95,80]
>>> max of scores
95
>>> min of scores
68

# abs: remove sign
>>> abs of -7
7
>>> abs of 7
7
>>> abs of 0
0

# Clamp: keep value in [low, high]
This is how to clamp of x and low and high:
   The answer is max of low and (min of x and high)
Now you know

>>> clamp of 5 and 0 and 10
5
>>> clamp of 15 and 0 and 10
10
>>> clamp of -3 and 0 and 10
0
```

```bridget
Use the standard library
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
Use the standard library
# Three ways to return multiple values from a function
#
#   1. Return an array:  [a, b]              access with item 0 in r, item 1 in r
#   2. Return an object: {"q": ..., "r": …}  access with item "q" in r
#   3. Implicit return:  omit The answer is  — all locals bundled as an object

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
# Do nothing demo
# Use when a branch deliberately takes no action,
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
# Quadratic equation ax^2 + bx + c = 0 (assumes two real roots)
# Formula: x = (-b ± √D) / 2a,  D = b^2 - 4ac
# Returns [larger root, smaller root]

This is how to solve of a and b and c:
   Remember that D is diff of (product of b and b) and (product of 4 and (product of a and c))
   Remember that sqrtD is sqrt of D
   Remember that denom is tofloat of (product of 2 and a)
   Remember that mb is tofloat of (diff of 0 and b)
   Remember that x1 is quotient of (sum of mb and sqrtD) and denom
   Remember that x2 is quotient of (diff of mb and sqrtD) and denom
   The answer is [x1, x2]
Now you know

# Test: x^2 - 3x + 2 = 0 → x = 2, 1
>>> solve of 1 and -3 and 2
[2.000000, 1.000000]
# Test: x^2 - 1 = 0 → x = 1, -1
>>> solve of 1 and 0 and -1
[1.000000, -1.000000]
# Test: x^2 - 4 = 0 → x = 2, -2
>>> solve of 1 and 0 and -4
[2.000000, -2.000000]
# Test: x^2 - 5x + 6 = 0 → x = 3, 2
>>> solve of 1 and -5 and 6
[3.000000, 2.000000]
```

```bridget
Use the standard library
# 1D random walk: start at 0, take N steps of +1 or -1 (50% each)
# Returns final position.

This is how to walk of N:
   Remember that pos is 0
   Do this N times:
      Remember that step is random, do it
      When step is less than 0.5, then:
         Decrease pos
      But, if not:
         Increase pos
      End when
   End do
   The answer is pos
Now you know

# Test: 0 steps → always 0
>>> walk of 0
0
# Test: parity of |result| matches parity of N (each step is ±1)
# Even steps → even result
>>> remainder of (abs of (walk of 10)) and 2
0
# Odd steps → odd result
>>> remainder of (abs of (walk of 7)) and 2
1
```

```bridget
Use the standard library
# Reverse an array by swapping from both ends toward the center

This is how to reverse of A:
   Remember that n is A's length
   Remember that half is quotient of n and 2
   Remember that i is 0
   Do this half times:
      Remember that j is diff of (diff of n and 1) and i
      Remember that tmp is item i in A
      Remember that item i in A is item j in A
      Remember that item j in A is tmp
      Increase i
   End do
   The answer is A
Now you know

# Test: odd length
>>> reverse of [1,2,3,4,5]
[5, 4, 3, 2, 1]
# Test: even length
>>> reverse of [1,2,3,4]
[4, 3, 2, 1]
# Test: single element
>>> reverse of [42]
[42]
# Test: empty array
>>> reverse of []
[]
# Test: string (stored as char-code array, same operation)
>>> reverse of "hello"
"olleh"
```

```bridget
Use the standard library
# ROT13: rotate each letter 13 places — the classic self-inverse cipher
# Strings are stored as character-code arrays.
# Char codes: 'A'=65  'Z'=90  'a'=97  'z'=122
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

# Test: uppercase  ABC → NOP
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
# Count scores >= 60 from a list, skipping invalid values (< 0 or > 100)
#
# Method 1: nested When (invert skip conditions)
# Method 2: skip flag (avoids deep nesting)
#
# Bridget comparison reminder (counterintuitive):
#   "is at most N"  means >= N
#   "is at least N" means <= N

# === Method 1: nested When ===
This is how to count_pass_v1 of scores:
   Remember that count is 0
   Remember that n is scores's length
   Remember that i is 0
   Do this n times:
      Remember that x is item i in scores
      When x is at most 0, then:
         When x is at least 100, then:
            When x is at most 60, then:
               Increase count
            End when
         End when
      End when
      Increase i
   End do
   The answer is count
Now you know

# === Method 2: skip flag ===
This is how to count_pass_v2 of scores:
   Remember that count is 0
   Remember that n is scores's length
   Remember that i is 0
   Do this n times:
      Remember that x is item i in scores
      Remember that skip is 0
      When x is less than 0, then:
         Remember that skip is 1
      End when
      When x is more than 100, then:
         Remember that skip is 1
      End when
      When x is less than 60, then:
         Remember that skip is 1
      End when
      When skip is 0, then:
         Increase count
      End when
      Increase i
   End do
   The answer is count
Now you know

# Test: [85,60,59,100,-1,120,72] → 85,60,100,72 pass = 4
>>> count_pass_v1 of [85,60,59,100,-1,120,72]
4
>>> count_pass_v2 of [85,60,59,100,-1,120,72]
4
# Test: all failing
>>> count_pass_v1 of [10,20,30]
0
>>> count_pass_v2 of [10,20,30]
0
# Test: all invalid
>>> count_pass_v1 of [-1,-5,200]
0
>>> count_pass_v2 of [-1,-5,200]
0
# Test: empty array
>>> count_pass_v1 of []
0
>>> count_pass_v2 of []
0
# Test: boundary values (60 and 100 both pass, 0 is in range but fails)
>>> count_pass_v1 of [0,60,100]
2
>>> count_pass_v2 of [0,60,100]
2
```

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
>>> run of [["PUSH",3],["PUSH",4],["ADD",0]]
7
# Test: (3 + 4) * 2 = 14
>>> run of [["PUSH",3],["PUSH",4],["ADD",0],["PUSH",2],["MUL",0]]
14
# Test: 10 - (2 + 3) = 5
>>> run of [["PUSH",10],["PUSH",2],["PUSH",3],["ADD",0],["SUB",0]]
5
# Test: DUP 5 then multiply → 25
>>> run of [["PUSH",5],["DUP",0],["MUL",0]]
25
# Test: POP discards the top → 7
>>> run of [["PUSH",7],["PUSH",99],["POP",0]]
7
# Test: single PUSH
>>> run of [["PUSH",42]]
42
```

```bridget
Use the standard library
# Find the first occurrence of sub in s (0-based index), or -1 if not found
# Strings are stored as char-code arrays.

This is how to find of s and sub:
   Remember that n is s's length
   Remember that m is sub's length
   Remember that neg1 is diff of 0 and 1
   Remember that pos is neg1
   When m is 0, then:
      Remember that pos is 0
   But, if not:
      When n is less than m, then:
         Do nothing
      But, if not:
         Remember that limit is sum of (diff of n and m) and 1
         Remember that i is 0
         Do this limit times:
            When pos is neg1, then:
               Remember that match is 1
               Remember that j is 0
               Do this m times:
                  Remember that ij is sum of i and j
                  Remember that cs is item ij in s
                  Remember that ct is item j in sub
                  When cs is not ct, then:
                     Remember that match is 0
                  End when
                  Increase j
               End do
               When match is 1, then:
                  Remember that pos is i
               End when
            End when
            Increase i
         End do
      End when
   End when
   The answer is pos
Now you know

# Test: simple match
>>> find of "hello world" and "world"
6
# Test: match at start
>>> find of "hello" and "hello"
0
# Test: single character
>>> find of "hello" and "l"
2
# Test: not found
>>> find of "hello" and "xyz"
-1
# Test: empty sub → 0
>>> find of "hello" and ""
0
# Test: sub longer than s
>>> find of "hi" and "hello"
-1
# Test: match near end
>>> find of "abcde" and "de"
3
```

```bridget
Use the standard library
# Replace all occurrences of old in s with repl
# If old is empty, return s unchanged (prevents infinite loop)
# Strings are stored as char-code arrays.
#
# Bridget comparison reminder:
#   "is at most N"  means >= N
#   "is at least N" means <= N

This is how to replace of s and old and repl:
   Remember that result is ""
   Remember that n is s's length
   Remember that m is old's length
   Remember that replen is repl's length
   When m is 0, then:
      The answer is s
   End when
   Remember that i is 0
   Remember that limit is sum of n and 1
   Do this limit times:
      When i is at most n, then:
         Leave the loop
      End when
      Remember that match is 0
      Remember that tail is sum of i and m
      When tail is at least n, then:
         Remember that match is 1
         Remember that j is 0
         Do this m times:
            Remember that ij is sum of i and j
            Remember that cs is item ij in s
            Remember that co is item j in old
            When cs is not co, then:
               Remember that match is 0
            End when
            Increase j
         End do
      End when
      When match is 1, then:
         Remember that k is 0
         Do this replen times:
            Add result to (item k in repl)
            Increase k
         End do
         Remember that i is sum of i and m
      But, if not:
         Add result to (item i in s)
         Increase i
      End when
   End do
   The answer is result
Now you know

# Test: simple replacement
>>> replace of "hello world" and "world" and "Yui"
"hello Yui"
# Test: multiple replacements
>>> replace of "ababab" and "a" and "X"
"XbXbXb"
# Test: shorter replacement
>>> replace of "hello hello" and "hello" and "hi"
"hi hi"
# Test: longer replacement
>>> replace of "abc" and "b" and "BBB"
"aBBBc"
# Test: no match → original unchanged
>>> replace of "hello" and "xyz" and "ABC"
"hello"
# Test: full string replaced
>>> replace of "foo" and "foo" and "bar"
"bar"
# Test: delete (empty replacement)
>>> replace of "a-b-c" and "-" and ""
"abc"
# Test: empty old → return original
>>> replace of "hello" and "" and "X"
"hello"
```

```bridget
Use the standard library
# Type conversion functions

# tostring: any value → string (char-code array)
>>> tostring of 42
"42"
>>> tostring of 3.14
"3.140000"

# toarray: string → explicit char-code array view
>>> toarray of "Hi"
[72, 105]
>>> toarray of "ABC"
[65, 66, 67]

# Reverse conversions: string → number
>>> toint of "100"
100
>>> tofloat of "3.14"
3.140000

# Combine tostring and length to count digits
This is how to digits of n:
   Remember that s is tostring of n
   The answer is s's length
Now you know

>>> digits of 7
1
>>> digits of 100
3
>>> digits of 123456
6
```

```bridget
Use the standard library
# Classify a triangle from three side lengths:
#   "not_triangle" : violates triangle inequality (a+b > c, etc.)
#   "equilateral"  : all three sides equal
#   "isosceles"    : exactly two sides equal
#   "scalene"      : all sides different
#
# Bridget: "is at least N" means <= N — used for triangle inequality check.

This is how to classify of a and b and c:
   Remember that ok is 1
   Remember that ab is sum of a and b
   Remember that ac is sum of a and c
   Remember that bc is sum of b and c
   When ab is at least c, then:
      Remember that ok is 0
   End when
   When ac is at least b, then:
      Remember that ok is 0
   End when
   When bc is at least a, then:
      Remember that ok is 0
   End when
   When ok is 0, then:
      The answer is "not_triangle"
   End when
   Remember that eq is 0
   Remember that dab is diff of a and b
   Remember that dbc is diff of b and c
   Remember that dac is diff of a and c
   When dab is 0, then:
      Increase eq
   End when
   When dbc is 0, then:
      Increase eq
   End when
   When dac is 0, then:
      Increase eq
   End when
   When eq is 3, then:
      The answer is "equilateral"
   End when
   When eq is 1, then:
      The answer is "isosceles"
   End when
   The answer is "scalene"
Now you know

# Test: equilateral
>>> classify of 5 and 5 and 5
"equilateral"
# Test: isosceles
>>> classify of 5 and 5 and 8
"isosceles"
>>> classify of 8 and 5 and 5
"isosceles"
>>> classify of 5 and 8 and 5
"isosceles"
# Test: scalene
>>> classify of 3 and 4 and 5
"scalene"
>>> classify of 7 and 8 and 9
"scalene"
# Test: triangle inequality violated
>>> classify of 1 and 2 and 3
"not_triangle"
>>> classify of 1 and 1 and 5
"not_triangle"
>>> classify of 10 and 1 and 1
"not_triangle"
# Test: degenerate (collinear) → not a triangle
>>> classify of 2 and 2 and 4
"not_triangle"
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
# Find unique characters in a string, preserving order of first occurrence
# Strings are stored as char-code arrays, so "is not in" works for membership.

This is how to unique_chars of s:
   Remember that result is ""
   Remember that i is 0
   Do this s's length times:
      Remember that c is item i in s
      When c is not in result, then:
         Add result to c
      End when
      Increase i
   End do
   The answer is result
Now you know

# Test: collapse duplicates
>>> unique_chars of "banana"
"ban"
>>> unique_chars of "mississippi"
"misp"
# Test: order is preserved
>>> unique_chars of "abcabc"
"abc"
>>> unique_chars of "programming"
"progamin"
# Test: all same character
>>> unique_chars of "aaaa"
"a"
# Test: empty string
>>> unique_chars of ""
""
```
