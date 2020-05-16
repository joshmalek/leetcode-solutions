# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements. You must 
# do this in-place without making a copy of the array.

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

# Notes:
# First idea: Iterate through the array, and count and delete every zero encountered.  At 
# the end of the array, append the number of zeros counted.  This is O(n) time, and O(1) space.


from typing import List
def moveZeroes(nums: List[int]) -> None:
    i = 0
    count = 0
    while(i < len(nums)):
        if(nums[i]==0):
            del nums[i]
            print(nums)
            count += 1
        else:
            i+=1
    for x in range(0,count):
        nums.append(0)
    print(nums)

moveZeroes([0,1,0,3,12])
