# Given a 32-bit signed integer, reverse digits of an integer.

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

# Notes:
# First thoughts: I could convert it to a string and maybe reverse it that way. I'm thinking of using the
# 2 pointer method from the reverseString problem, but I think this is an ugly solution.

# In any case, first need to get the sign (compare against 0). Then, pop off the last digit, and added
# to the new string number.  At the end, convert to an int.  This technically is O(n), and O(n) space,
# but it is not a good solution.  Try to refine it in the future.
from typing import List
def reverse(x: int) -> int:
    if(x < 0):
        sign = -1
        x *= -1
    else:
        sign = 1

    x = str(x)
    x = list(x)
    rev = list()
    s = ""
    for i in range(0,len(x)):
        rev.append(x.pop())
    s = s.join(rev)
    s = int(s)
    s = s * sign
    if(s > pow(2,31)-1 or s < pow(-2,31)):
        return 0
    else:
        return s
print(reverse(-12300000))