# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Could you do it in-place with O(1) extra space?

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

# Notes:
# Start from nums[k:end] and insert, then insert nums[0:k]
# runtime: 0(n), space: 0(n)
# try to improve to O(1) space, cyclic dependencies (each element relies on another element)

from typing import List
def rotate(nums: List[int], k: int) -> None:
    new = nums[0:len(nums)-k]
    new2 = nums[len(nums)-k:]
    for i in range(0,len(new2)):
        nums[i] = new2[i]
    for x in range(0,len(new)):
        nums[x+len(new2)] = new[x]
    print(nums)

rotate([1,2,3,4,5,6,7],3)