```bridget
# 1: Factorial — import, funcdef/1-arg, assign, repeat, product, increment, return
Use the standard library
This is how to factorial of n:
   Remember that result is 1
   Remember that i is 1
   Do this n times:
      Remember that result is product of result and i
      Increase i
   End do
   The answer is result
Now you know
>>> factorial of 0
1
>>> factorial of 5
120
>>> factorial of 10
3628800
```

```bridget
# 2: In-place reversal — Remember that item i in arr is val (index write), Increase + Decrease, diff
Use the standard library
This is how to reverse_array of arr:
   Remember that n is arr's length
   Remember that left is 0
   Remember that right is diff of n and 1
   Do this n times:
      When left is at most right, then:
         Leave the loop
      End when
      Remember that tmp is item left in arr
      Remember that item left in arr is item right in arr
      Remember that item right in arr is tmp
      Increase left
      Decrease right
   End do
   The answer is arr
Now you know
>>> reverse_array of [1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
>>> reverse_array of [1, 2]
[2, 1]
>>> reverse_array of [42]
[42]
>>> reverse_array of []
[]
```

```bridget
# 3: FizzBuzz — is (==), is not (!=), remainder, if/else, append, tostring, array literal
Use the standard library
This is how to fizzbuzz of n:
   Remember that result is []
   Remember that i is 1
   Do this n times:
      When remainder of i and 3 is 0, then:
         When remainder of i and 5 is 0, then:
            Add result to "FizzBuzz"
         But, if not:
            Add result to "Fizz"
         End when
      But, if not:
         When remainder of i and 5 is not 0, then:
            Add result to tostring of i
         But, if not:
            Add result to "Buzz"
         End when
      End when
      Increase i
   End do
   The answer is result
Now you know
>>> fizzbuzz of 5
["1", "2", "Fizz", "4", "Buzz"]
>>> fizzbuzz of 15
["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
```

```bridget
# 4: Clamp — funcdef/3-args, if without else, is less than, is more than
This is how to clamp of x and lo and hi:
   When x is less than lo, then:
      The answer is lo
   End when
   When x is more than hi, then:
      The answer is hi
   End when
   The answer is x
Now you know
>>> clamp of 5 and 0 and 10
5
>>> clamp of -3 and 0 and 10
0
>>> clamp of 15 and 0 and 10
10
```

```bridget
# 5: Count elements <= limit — is at least (<=), length, item-in indexing
This is how to count_le of arr and limit:
   Remember that count is 0
   Remember that i is 0
   Do this arr's length times:
      When item i in arr is at least limit, then:
         Increase count
      End when
      Increase i
   End do
   The answer is count
Now you know
>>> count_le of [1, 2, 3, 4, 5] and 3
3
>>> count_le of [10, 20, 30] and 25
2
>>> count_le of [] and 5
0
```

```bridget
# 6: First index >= limit — is at most (>=), Leave the loop
This is how to first_ge of arr and limit:
   Remember that found is -1
   Remember that i is 0
   Do this arr's length times:
      When item i in arr is at most limit, then:
         Remember that found is i
         Leave the loop
      End when
      Increase i
   End do
   The answer is found
Now you know
>>> first_ge of [1, 2, 5, 3] and 4
2
>>> first_ge of [1, 2, 3] and 5
-1
>>> first_ge of [10, 20, 30] and 10
0
```

```bridget
# 7: Deduplicate — is not in, Add (append)
This is how to deduplicate of arr:
   Remember that result is []
   Remember that i is 0
   Do this arr's length times:
      Remember that val is item i in arr
      When val is not in result, then:
         Add result to val
      End when
      Increase i
   End do
   The answer is result
Now you know
>>> deduplicate of [1, 2, 1, 3, 2]
[1, 2, 3]
>>> deduplicate of [5, 5, 5]
[5]
>>> deduplicate of []
[]
```

```bridget
# 8: Greet — funcdef no-arg (^^), string interpolation, Now (print), Stop here, funcname do it
This is how to hello ^^:
   Now, "Hello, World!"
   Stop here
Now you know
This is how to greet of name:
   The answer is "Hello, {name}!"
Now you know
>>> hello, do it
Nothing
>>> greet of "Alice"
"Hello, Alice!"
>>> greet of "Bob"
"Hello, Bob!"
```

```bridget
# 9: Safe quotient — Do nothing (pass), Nothing (null), is (==), quotient
Use the standard library
This is how to safe_q of a and b:
   When b is 0, then:
      Do nothing
   But, if not:
      The answer is quotient of a and b
   End when
   The answer is Nothing
Now you know
>>> safe_q of 10 and 2
5
>>> safe_q of 9 and 3
3
>>> safe_q of 7 and 0
Nothing
```

```bridget
# 10: Object literal, item "key" in obj read/write, tofloat, sqrt, float literal
Use the standard library
# 2D point stored as an object {"x": float, "y": float}

This is how to make_point of x and y:
   The answer is {"x": tofloat of x, "y": tofloat of y}
Now you know

This is how to distance of p and q:
   Remember that dx is diff of (item "x" in p) and (item "x" in q)
   Remember that dy is diff of (item "y" in p) and (item "y" in q)
   The answer is sqrt of (sum of (product of dx and dx) and (product of dy and dy))
Now you know

Remember that origin is make_point of 0 and 0
Remember that A is make_point of 3 and 4
>>> item "x" in A
3.000000
>>> item "y" in A
4.000000
>>> distance of origin and A
5.000000

# Write to an object key
Remember that item "x" in A is 0.0
>>> item "x" in A
0.000000
>>> distance of origin and A
4.000000
```

```bridget
# 11: Membership test — backtick extra-name, is in, Yes/No (boolean), Nothing (null)
This is how to `is member` of val and collection:
   When val is in collection, then:
      The answer is Yes
   But, if not:
      The answer is No
   End when
Now you know
>>> `is member` of 2 and [1, 2, 3]
Yes
>>> `is member` of 5 and [1, 2, 3]
No
>>> `is member` of Nothing and [1, Nothing, 3]
Yes
```

```bridget
# 12: Integer as bit array — item i in integer, integer's length, [bit-array] is integer
Use the standard library
# In Bridget, integers are stored as bit arrays (LSB first).
# item 0 in N → LSB of N,  N's length → number of bits needed.
# A bit-array literal compares equal to its integer: [0, 1, 1] is 6 → Yes.

# Count set bits (popcount / Hamming weight)
This is how to popcount of n:
   Remember that count is 0
   Remember that i is 0
   Do this n's length times:
      When item i in n is 1, then:
         Increase count
      End when
      Increase i
   End do
   The answer is count
Now you know

# 6 = 0b110 → stored as [0, 1, 1] (LSB first). A bit-array literal equals its integer.
>>> item 0 in 6
0
>>> item 1 in 6
1
>>> item 2 in 6
1
>>> 6's length
3
>>> popcount of 7
3
>>> popcount of 6
2
>>> popcount of 255
8
```
