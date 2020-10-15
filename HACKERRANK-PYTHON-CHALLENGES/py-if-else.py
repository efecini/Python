"""
Python If-Else


Check Tutorial tab to know how to to solve.

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
Explanation 1


 and  is even, so it is not weird.
 """

if __name__ == '__main__':
    
    n = int(input().strip())
    # One-liner.
    # Works on VSCode but doesn't work in hackerrank's online editor.
    print("Weird") if n%2 != 0 else print("Not Weird") if n in range(2, 6) or n > 20 else print("Weird")