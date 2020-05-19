# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

# Notes:
# The easy way to do this would be a[::-1] to reverse an array in Python, but this is a Python
# only solution.  A better way to look at this is to use a 2 pointer approach, and swap accordingly.
# First, calculate whether there is an odd or even number of indices, and then swap the indices.

from typing import List
def reverseString(s: List[str]) -> None:
    # Option 1
    # s = s[::-1]

    # Option 2
    # Remember, // does floor division in Python3
    maxi = len(s)//2
    for i in range(0,maxi):
        temp = s[len(s)-1-i]
        s[len(s)-1-i] = s[i]
        s[i] = temp
    print(s)

reverseString(['a','b','c','d'])