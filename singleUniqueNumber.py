# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

# Notes:
# Initial idea is to run 2 pointer approach, for each ith element inspect every other element to see if 
# there is a match.  If there isn't, this is the number to return.  Worst case is O(n^2).
#
# Second thought is to sort the array and run 2 pointer again.  This would be faster, as the array would
# only need to be iterated through once, but also need to be sorted.  This would be O(nlogn), so not optimal.
# 
# Third idea is create a dictionary, with the key being the element and the value the number of times 
# it has been seen.  Then, just return the element with a value of 1.  This is O(n) to search through 
# the array, and O(n) to search through the dictionary.  Space is O(n) as well.  This is suboptimal
# because of memory usage.

from typing import List
def singleNumber(nums: List[int]) -> int:
    seen = dict()
    for i in nums:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1
    for num in seen.keys():
        if(seen[num] == 1):
            return num
    return 0

print(singleNumber([0,0,1,2,2]))