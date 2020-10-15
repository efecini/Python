"""
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
"""
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    weird = "Weird"
    not_weird = "Not Weird"

    n = int(input().strip())
    #One-Liner is always better.
    print(weird) if (n%2) != 0 or (n in range(6, 21)) else print(not_weird)
"""
    if n%2 != 0:
        print(weird)
    else:
        if n in range(2, 6) or n>20:
            print(not_weird)
        elif n in range(6, 21):
            print(weird)
"""


