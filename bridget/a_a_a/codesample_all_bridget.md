```bridget
Use the standard library
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
>>> bin_to_int of "0" 
0
>>> bin_to_int of "1" 
1
>>> bin_to_int of "10" 
2
>>> bin_to_int of "11" 
3
>>> bin_to_int of "1011" 
11
>>> bin_to_int of "11111111" 
255
>>> bin_to_int of "100000000" 
256
>>> bin_to_int of "0001010" 
10
>>> bin_to_int of "" 
0
```

```bridget
This is how to bits_add of A and B:
   Remember that max is A's length
   When B's length is more than max, then:
      Remember that max is B's length
   End when
   Increase max
   Remember that c is 0
   Remember that X is 0
   Remember that index is 0
   Do this max times:
      When index is less than A's length, then:
         Remember that a is item index in A
      But, if not:
         Remember that a is 0
      End when
      When index is less than B's length, then:
         Remember that b is item index in B
      But, if not:
         Remember that b is 0
      End when
      Remember that sum is 0
      When a is 1, then:
         Increase sum
      End when
      When b is 1, then:
         Increase sum
      End when
      When c is 1, then:
         Increase sum
      End when
      When sum is 0, then:
         Remember that x is 0
         Remember that c is 0
      End when
      When sum is 1, then:
         Remember that x is 1
         Remember that c is 0
      End when
      When sum is 2, then:
         Remember that x is 0
         Remember that c is 1
      End when
      When sum is 3, then:
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
>>> bits_and of 6 and 0 
0
This is how to bits_or of A and B:
   Remember that n is A's length
   When B's length is more than n, then:
      Remember that n is B's length
   End when
   Remember that i is 0
   Remember that X is 0
   Do this n times:
      Remember that a is 0
      When i is less than A's length, then:
         Remember that a is item i in A
      End when
      Remember that b is 0
      When i is less than B's length, then:
         Remember that b is item i in B
      End when
      Remember that x is 0
      When a is 1, then:
         Remember that x is 1
      End when
      When b is 1, then:
         Remember that x is 1
      End when
      Add X to x
      Increase i
   End do
   The answer is X
Now you know
>>> bits_or of 6 and 5 
7
>>> bits_or of 4 and 3 
7
>>> bits_or of 0 and 5 
5
This is how to bits_xor of A and B:
   Remember that n is A's length
   When B's length is more than n, then:
      Remember that n is B's length
   End when
   Remember that i is 0
   Remember that X is 0
   Do this n times:
      Remember that a is 0
      When i is less than A's length, then:
         Remember that a is item i in A
      End when
      Remember that b is 0
      When i is less than B's length, then:
         Remember that b is item i in B
      End when
      Remember that sum is 0
      When a is 1, then:
         Increase sum
      End when
      When b is 1, then:
         Increase sum
      End when
      Remember that x is 0
      When sum is 1, then:
         Remember that x is 1
      End when
      Add X to x
      Increase i
   End do
   The answer is X
Now you know
>>> bits_xor of 6 and 5 
3
>>> bits_xor of 3 and 3 
0
>>> bits_xor of 0 and 7 
7
```

```bridget
Use the standard library
This is how to lshift of n and k:
   Remember that result is n
   Do this k times:
      Remember that result is product of result and 2
   End do
   The answer is result
Now you know
This is how to rshift of n and k:
   Remember that result is n
   Do this k times:
      Remember that result is quotient of result and 2
   End do
   The answer is result
Now you know
>>> lshift of 1 and 3 
8
>>> lshift of 3 and 2 
12
>>> lshift of 5 and 1 
10
>>> lshift of 7 and 0 
7
>>> rshift of 7 and 0 
7
>>> rshift of 8 and 3 
1
>>> rshift of 12 and 2 
3
>>> rshift of 13 and 2 
3
>>> rshift of 5 and 3 
0
>>> lshift of 0 and 5 
0
>>> rshift of 0 and 5 
0
>>> rshift of (lshift of 11 and 4) and 4 
11
```

```bridget
Use the standard library
This is how to bmi_category of w and h:
   Remember that weight is tofloat of w
   Remember that h2 is product of h and h
   Remember that bmi is quotient of weight and h2
   When bmi is less than 18.500000, then:
      The answer is "Underweight"
   End when
   When bmi is less than 25, then:
      The answer is "Normal"
   End when
   When bmi is less than 30, then:
      The answer is "Overweight"
   End when
   The answer is "Obese"
Now you know
>>> bmi_category of 50 and 1.700000 
"Underweight"
>>> bmi_category of 65 and 1.700000 
"Normal"
>>> bmi_category of 80 and 1.700000 
"Overweight"
>>> bmi_category of 100 and 1.700000 
"Obese"
>>> bmi_category of 55 and 1.600000 
"Normal"
>>> bmi_category of 90 and 1.650000 
"Obese"
>>> bmi_category of 45 and 1.700000 
"Underweight"
```

```bridget
Use the standard library
This is how to bubble_sort of A:
   Remember that n is A's length
   Do this n times:
      Remember that i is 0
      Do this diff of n and 1 times:
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
>>> bubble_sort of [3, 1, 4, 1, 5, 9, 2, 6] 
[1, 1, 2, 3, 4, 5, 6, 9]
>>> bubble_sort of [5, 4, 3, 2, 1] 
[1, 2, 3, 4, 5]
>>> bubble_sort of [1, 2, 3] 
[1, 2, 3]
>>> bubble_sort of [42] 
[42]
>>> bubble_sort of [] 
[]
```

```bridget
Use the standard library
This is how to closest of arr and target:
   Remember that n is arr's length
   Remember that best is item 0 in arr
   Remember that bestd is abs of (diff of best and target)
   Remember that i is 1
   Do this diff of n and 1 times:
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
>>> closest of [1, 5, 9, 12, 20] and 10 
9
>>> closest of [1, 5, 9, 12, 20] and 11 
12
>>> closest of [1, 5, 9, 12, 20] and 6 
5
>>> closest of [42] and 100 
42
>>> closest of [-5, -2, 3, 8] and 0 
-2
>>> closest of [1, 2, 3, 4, 5] and 3 
3
>>> closest of [1, 3] and 2 
1
```

```bridget
Use the standard library
This is how to compound of P and r and n:
   Remember that balance is tofloat of P
   Remember that factor is sum of (tofloat of 1) and r
   Do this n times:
      Remember that balance is product of balance and factor
   End do
   The answer is balance
Now you know
This is how to years_to_double of r:
   Remember that balance is tofloat of 1
   Remember that factor is sum of (tofloat of 1) and r
   Remember that n is 0
   Do this 1000 times:
      When balance is at least 2, then:
         Leave the loop
      End when
      Remember that balance is product of balance and factor
      Increase n
   End do
   The answer is n
Now you know
>>> compound of 1000 and 0.050000 and 1 
1050.000000
>>> compound of 1000 and 0.050000 and 2 
1102.500000
>>> compound of 1000 and 0.100000 and 3 
1331.000000
>>> compound of 100 and 0.000000 and 5 
100.000000
>>> compound of 1000 and 0.050000 and 0 
1000.000000
>>> years_to_double of 0.100000 
8
>>> years_to_double of 0.070000 
11
>>> years_to_double of 0.050000 
15
```

```bridget
Use the standard library
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
This is how to count_dice of N:
   Remember that counts is [0, 0, 0, 0, 0, 0]
   Do this N times:
      Remember that r is toint of (product of (random, do it) and 6)
      Increase item r in counts
   End do
   The answer is counts
Now you know
Now, count_dice of 60
Now, count_dice of 600
>>> count_dice of 0 
[0, 0, 0, 0, 0, 0]
>>> sum of (count_dice of 60) 
60
>>> sum of (count_dice of 1000) 
1000
```

```bridget
Use the standard library
This is how to distance of x1 and y1 and x2 and y2:
   Remember that dx is diff of x2 and x1
   Remember that dy is diff of y2 and y1
   Remember that d2 is sum of (product of dx and dx) and (product of dy and dy)
   The answer is sqrt of d2
Now you know
>>> distance of 0 and 0 and 3 and 4 
5.000000
>>> distance of 7 and 7 and 7 and 7 
0.000000
>>> distance of -1 and 0 and 2 and 4 
5.000000
>>> distance of 0 and 0 and 5 and 12 
13.000000
```

```bridget
Use the standard library
This is how to dot of a and b:
   Remember that total is 0
   Remember that n is a's length
   Remember that i is 0
   Do this n times:
      Remember that total is sum of total and (product of item i in a and item i in b)
      Increase i
   End do
   The answer is total
Now you know
>>> dot of [1, 2, 3] and [4, 5, 6] 
32
>>> dot of [1, 0, 0] and [0, 1, 0] 
0
>>> dot of [2, 3] and [2, 3] 
13
>>> dot of [1, 2, 3, 4] and [1, 1, 1, 1] 
10
>>> dot of [] and [] 
0
>>> dot of [2, -3] and [-1, 4] 
-14
```

```bridget
Use the standard library
This is how to grade of score:
   Remember that result is "F"
   When score is at least 90, then:
      Remember that result is "A"
   But, if not:
      When score is at least 80, then:
         Remember that result is "B"
      But, if not:
         When score is at least 70, then:
            Remember that result is "C"
         But, if not:
            When score is at least 60, then:
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
This is how to passed of score:
   Remember that g is grade of score
   When g is not "F", then:
      The answer is yes
   But, if not:
      The answer is no
   End when
Now you know
>>> passed of 75 
yes
>>> passed of 40 
no
```

```bridget
Use the standard library
This is how to motto ^^:
   The answer is "Keep going today!"
Now you know
>>> motto, do it 
"Keep going today!"
This is how to greet of name:
   The answer is "Hello, {name}!"
Now you know
>>> greet of "Yui" 
"Hello, Yui!"
This is how to score_msg of name and points:
   The answer is "Score of {name}: {points} points"
Now you know
>>> score_msg of "Taro" and 95 
"Score of Taro: 95 points"
>>> tostring of 42 
"42"
```

```bridget
Use the standard library
This is how to leap_year of y:
   Remember that r400 is remainder of y and 400
   When r400 is 0, then:
      The answer is yes
   End when
   Remember that r100 is remainder of y and 100
   When r100 is 0, then:
      The answer is no
   End when
   Remember that r4 is remainder of y and 4
   When r4 is 0, then:
      The answer is yes
   End when
   The answer is no
Now you know
>>> leap_year of 2000 
yes
>>> leap_year of 1600 
yes
>>> leap_year of 1900 
no
>>> leap_year of 2100 
no
>>> leap_year of 1700 
no
>>> leap_year of 2024 
yes
>>> leap_year of 2020 
yes
>>> leap_year of 1996 
yes
>>> leap_year of 2023 
no
>>> leap_year of 2025 
no
>>> leap_year of 2001 
no
```

```bridget
Use the standard library
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
>>> leibniz of 1 
4.000000
>>> leibniz of 2 
2.666667
>>> leibniz of 4 
2.895238
>>> leibniz of 100 
3.131593
>>> leibniz of 1000 
3.140593
```

```bridget
Use the standard library
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
               Add row to item j in item i in M
            End when
            Increase j
         End do
         Add result to row
      End when
      Increase i
   End do
   The answer is result
Now you know
This is how to det of M:
   Remember that n is M's length
   When n is 1, then:
      The answer is item 0 in item 0 in M
   End when
   Remember that total is 0
   Remember that j is 0
   Do this n times:
      Remember that cof is product of item j in item 0 in M and (det of (minor of M and 0 and j))
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
>>> det of [[5]] 
5
>>> det of [[-3]] 
-3
>>> det of [[1, 2], [3, 4]] 
-2
>>> det of [[1, 0], [0, 1]] 
1
>>> det of [[1, 2, 3], [4, 5, 6], [7, 8, 10]] 
-3
>>> det of [[1, 0, 0], [0, 1, 0], [0, 0, 1]] 
1
>>> det of [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]] 
24
>>> det of [[1, 2, 3], [2, 4, 6], [7, 8, 9]] 
0
```

```bridget
Use the standard library
>>> max of 3 and 1 and 4 and 1 and 5 and 9 and 2 and 6 
9
>>> min of 3 and 1 and 4 and 1 and 5 and 9 and 2 and 6 
1
Remember that scores is [72, 85, 90, 68, 95, 80]
>>> max of scores 
95
>>> min of scores 
68
>>> abs of -7 
7
>>> abs of 7 
7
>>> abs of 0 
0
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
Remember that menu is ["curry", "ramen", "sushi", "soba"]
This is how to check of item:
   When item is in menu, then:
      The answer is "available"
   But, if not:
      The answer is "not available"
   End when
Now you know
>>> check of "sushi" 
"available"
>>> check of "pizza" 
"not available"
Remember that allergy is ["egg", "soba", "wheat"]
This is how to safe of food:
   When food is not in allergy, then:
      The answer is yes
   But, if not:
      The answer is no
   End when
Now you know
>>> safe of "curry" 
yes
>>> safe of "soba" 
no
>>> safe of "egg" 
no
```

```bridget
Use the standard library
This is how to divmod_array of a and b:
   Remember that q is quotient of a and b
   Remember that r is remainder of a and b
   The answer is [q, r]
Now you know
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
This is how to point of x and y:
   Do nothing
Now you know
>>> divmod_array of 17 and 5 
[3, 2]
>>> divmod_array of 20 and 4 
[5, 0]
Remember that qr is divmod_array of 17 and 5
>>> item 0 in qr 
3
>>> item 1 in qr 
2
Remember that s is stats of [3, 1, 4, 1, 5, 9, 2, 6]
>>> item "min" in s 
1
>>> item "max" in s 
9
>>> item "sum" in s 
31
>>> item "count" in s 
8
Remember that P is point of 3 and 5
>>> item "x" in P 
3
>>> item "y" in P 
5
```

```bridget
Use the standard library
This is how to sign of n:
   Remember that result is ""
   When n is 0, then:
      
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
This is how to solve of a and b and c:
   Remember that D is diff of (product of b and b) and (product of 4 and (product of a and c))
   Remember that sqrtD is sqrt of D
   Remember that denom is tofloat of (product of 2 and a)
   Remember that mb is tofloat of (diff of 0 and b)
   Remember that x1 is quotient of (sum of mb and sqrtD) and denom
   Remember that x2 is quotient of (diff of mb and sqrtD) and denom
   The answer is [x1, x2]
Now you know
>>> solve of 1 and -3 and 2 
[2.000000, 1.000000]
>>> solve of 1 and 0 and -1 
[1.000000, -1.000000]
>>> solve of 1 and 0 and -4 
[2.000000, -2.000000]
>>> solve of 1 and -5 and 6 
[3.000000, 2.000000]
```

```bridget
Use the standard library
This is how to walk of N:
   Remember that pos is 0
   Do this N times:
      Remember that step is random, do it
      When step is less than 0.500000, then:
         Decrease pos
      But, if not:
         Increase pos
      End when
   End do
   The answer is pos
Now you know
>>> walk of 0 
0
>>> remainder of (abs of (walk of 10)) and 2 
0
>>> remainder of (abs of (walk of 7)) and 2 
1
```

```bridget
Use the standard library
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
>>> reverse of [1, 2, 3, 4, 5] 
[5, 4, 3, 2, 1]
>>> reverse of [1, 2, 3, 4] 
[4, 3, 2, 1]
>>> reverse of [42] 
[42]
>>> reverse of [] 
[]
>>> reverse of "hello" 
"olleh"
```

```bridget
Use the standard library
This is how to rot13 of s:
   Remember that result is ""
   Remember that n is s's length
   Remember that i is 0
   Do this n times:
      Remember that c is item i in s
      Remember that nc is c
      When c is at least 65, then:
         When c is at most 90, then:
            Remember that offset is diff of c and 65
            Remember that shifted is remainder of (sum of offset and 13) and 26
            Remember that nc is sum of shifted and 65
         End when
      End when
      When c is at least 97, then:
         When c is at most 122, then:
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
>>> rot13 of "ABC" 
"NOP"
>>> rot13 of "xyz" 
"klm"
>>> rot13 of "Hello, World!" 
"Uryyb, Jbeyq!"
>>> rot13 of "Uryyb, Jbeyq!" 
"Hello, World!"
>>> rot13 of "123 !?" 
"123 !?"
>>> rot13 of "" 
""
```

```bridget
Use the standard library
This is how to count_pass_v1 of scores:
   Remember that count is 0
   Remember that n is scores's length
   Remember that i is 0
   Do this n times:
      Remember that x is item i in scores
      When x is at least 0, then:
         When x is at most 100, then:
            When x is at least 60, then:
               Increase count
            End when
         End when
      End when
      Increase i
   End do
   The answer is count
Now you know
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
>>> count_pass_v1 of [85, 60, 59, 100, -1, 120, 72] 
4
>>> count_pass_v2 of [85, 60, 59, 100, -1, 120, 72] 
4
>>> count_pass_v1 of [10, 20, 30] 
0
>>> count_pass_v2 of [10, 20, 30] 
0
>>> count_pass_v1 of [-1, -5, 200] 
0
>>> count_pass_v2 of [-1, -5, 200] 
0
>>> count_pass_v1 of [] 
0
>>> count_pass_v2 of [] 
0
>>> count_pass_v1 of [0, 60, 100] 
2
>>> count_pass_v2 of [0, 60, 100] 
2
```

```bridget
Use the standard library
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
>>> run of [["PUSH", 3], ["PUSH", 4], ["ADD", 0]] 
7
>>> run of [["PUSH", 3], ["PUSH", 4], ["ADD", 0], ["PUSH", 2], ["MUL", 0]] 
14
>>> run of [["PUSH", 10], ["PUSH", 2], ["PUSH", 3], ["ADD", 0], ["SUB", 0]] 
5
>>> run of [["PUSH", 5], ["DUP", 0], ["MUL", 0]] 
25
>>> run of [["PUSH", 7], ["PUSH", 99], ["POP", 0]] 
7
>>> run of [["PUSH", 42]] 
42
```

```bridget
Use the standard library
This is how to find of s and sub:
   Remember that n is s's length
   Remember that m is sub's length
   Remember that neg1 is diff of 0 and 1
   Remember that pos is neg1
   When m is 0, then:
      Remember that pos is 0
   But, if not:
      When n is less than m, then:
         
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
>>> find of "hello world" and "world" 
6
>>> find of "hello" and "hello" 
0
>>> find of "hello" and "l" 
2
>>> find of "hello" and "xyz" 
-1
>>> find of "hello" and "" 
0
>>> find of "hi" and "hello" 
-1
>>> find of "abcde" and "de" 
3
```

```bridget
Use the standard library
This is how to replace of s and old and new:
   Remember that result is ""
   Remember that n is s's length
   Remember that m is old's length
   Remember that newlen is new's length
   When m is 0, then:
      The answer is s
   End when
   Remember that i is 0
   Remember that limit is sum of n and 1
   Do this limit times:
      When i is at least n, then:
         Leave the loop
      End when
      Remember that match is 0
      Remember that tail is sum of i and m
      When tail is at most n, then:
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
         Do this newlen times:
            Add result to item k in new
            Increase k
         End do
         Remember that i is sum of i and m
      But, if not:
         Add result to item i in s
         Increase i
      End when
   End do
   The answer is result
Now you know
>>> replace of "hello world" and "world" and "Yui" 
"hello Yui"
>>> replace of "ababab" and "a" and "X" 
"XbXbXb"
>>> replace of "hello hello" and "hello" and "hi" 
"hi hi"
>>> replace of "abc" and "b" and "BBB" 
"aBBBc"
>>> replace of "hello" and "xyz" and "ABC" 
"hello"
>>> replace of "foo" and "foo" and "bar" 
"bar"
>>> replace of "a-b-c" and "-" and "" 
"abc"
>>> replace of "hello" and "" and "X" 
"hello"
```

```bridget
Use the standard library
>>> tostring of 42 
"42"
>>> tostring of 3.140000 
"3.140000"
>>> toarray of "Hi" 
[72, 105]
>>> toarray of "ABC" 
[65, 66, 67]
>>> toint of "100" 
100
>>> tofloat of "3.14" 
3.140000
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
This is how to classify of a and b and c:
   Remember that ok is 1
   Remember that ab is sum of a and b
   Remember that ac is sum of a and c
   Remember that bc is sum of b and c
   When ab is at most c, then:
      Remember that ok is 0
   End when
   When ac is at most b, then:
      Remember that ok is 0
   End when
   When bc is at most a, then:
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
>>> classify of 5 and 5 and 5 
"equilateral"
>>> classify of 5 and 5 and 8 
"isosceles"
>>> classify of 8 and 5 and 5 
"isosceles"
>>> classify of 5 and 8 and 5 
"isosceles"
>>> classify of 3 and 4 and 5 
"scalene"
>>> classify of 7 and 8 and 9 
"scalene"
>>> classify of 1 and 2 and 3 
"not_triangle"
>>> classify of 1 and 1 and 5 
"not_triangle"
>>> classify of 10 and 1 and 1 
"not_triangle"
>>> classify of 2 and 2 and 4 
"not_triangle"
```

```bridget
Use the standard library
>>> isint of 42 
yes
>>> isint of 3.140000 
no
>>> isfloat of 3.140000 
yes
>>> isfloat of 42 
no
>>> isstring of "hello" 
yes
>>> isstring of 42 
no
>>> isarray of [1, 2, 3] 
yes
>>> isobject of {"x": 1} 
yes
>>> isobject of [1, 2, 3] 
no
>>> isbool of yes 
yes
>>> isbool of 1 
no
Remember that x is nothing
>>> isint of x 
no
>>> isstring of x 
no
>>> isarray of x 
no
```

```bridget
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
>>> unique_chars of "banana" 
"ban"
>>> unique_chars of "mississippi" 
"misp"
>>> unique_chars of "abcabc" 
"abc"
>>> unique_chars of "programming" 
"progamin"
>>> unique_chars of "aaaa" 
"a"
>>> unique_chars of "" 
""
>>> unique_chars of "sakurasakura" 
"sakur"
```
