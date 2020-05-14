# Given a sorted array nums, remove the duplicates in-place such that 
# each element appear only once and return the new length.

# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Notes:
# In-place = use a 2-pointer method as the array is already sorted. One pointer
# should keep track of the last unique element, and one for the current.

from typing import List
def removeDuplicates(nums: List[int]) -> int:
    pt1 = 0
    pt2 = 0
    while(pt2+1 < len(nums)):
        pt2+=1
        if(nums[pt1] != nums[pt2]):
            pt1+=1
            del nums[pt1:pt2]
            pt1 = pt2 - (pt2-pt1)
            pt2 = pt1

    #if the pointers aren't equal, then the program ended while in the delete stage
    if(pt1 != pt2):
        del nums[pt1:pt2]
    return len(nums)
        
print(removeDuplicates([1,1,2]))
print(removeDuplicates([1,1]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))