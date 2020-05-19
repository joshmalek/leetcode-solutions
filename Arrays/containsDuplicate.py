# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, 
# and it should return false if every element is distinct.

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

# Notes: 
# Initial approach is to look at each ith element, and scan the rest of the array for a duplicate.
# If there is a duplicate, return true. The downsides is that this is O(n^2) in the case that every
# integer is unique, and O(n) best case.  It's inefficient.
#
# Second approach is to sort the array and then iterate once through it.  Using the 2 pointer method,
# check each ith and i+1th index for equality.  Worst case (all unique) is O(nlogn), as sorting algorithm
# needs to run.  This is better than O(n^2).
#
# Weird way is convert the list to a set, which can only have unique values.  This will require space O(n).
# Compare the length of the set to the length of the list and return true if lengths aren't equal. 
# Converting the list to the set involves iterating over the list (O(n)) and adding each element 
# to the hash set (O(1)), so the total operation time is O(n).  Therefore, this is my best solution.
from typing import List
def containsDuplicate(nums: List[int]) -> bool:
    uniques = set(nums)
    return(len(nums)!=len(uniques))

print(containsDuplicate([1,2]))