# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

# Notes:
# Brute force: for each element, scan through the array to see if any other elements add to the target.  This would
# be O(n^2), and too inefficient for larger datasets.
# 
# Refined: Run through the array once and make a dictionary (key = element, value = index).  Then, run through the
# array again to see if target-element exists in the dictionary.  If it does, return the index. This will be O(n^2) 
# still I think due to the nested for loop.  Maybe refine further to not need the second for loop.

from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    indices = dict()
    for i, val in enumerate(nums):
        if(val in indices):
            indices[val].append(i)
        else:
            indices[val] = [i]
    for i,val in enumerate(nums):
        if(target-val in indices):
            for a in indices[target-val]:
                if(i != a):
                    return [i,a]
    
print(twoSum([3, 2, 4], 6))