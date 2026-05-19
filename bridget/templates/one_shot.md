Problem:
Check if two numbers in a list are closer than a given threshold.

>>> has_close_elements of [1, 2, 3] and 0.500000
0
>>> has_close_elements of [1, 2.800000, 3, 4, 5, 2] and 0.300000
1

### Answer
```bridget
Use the standard library
This is how to has_close_elements of numbers and threshold:
   Remember that length is numbers's length
   Remember that result is 0
   Remember that i is 0
   Do this length times:
      Remember that value1 is item i in numbers
      Remember that j is 0
      Do this length times:
         When i is not j, then:
            Remember that value2 is item j in numbers
            Remember that delta is diff of value1 and value2
            Remember that abs_delta is abs of delta
            When abs_delta is less than threshold, then:
               Remember that result is 1
            End when
         End when
         Increase j
      End do
      Increase i
   End do
   The answer is result
Now you know
```

Problem:
{PROBLEM}

### Answer
```bridget
