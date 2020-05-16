# Given two arrays, write a function to compute their intersection.
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

# Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

# Notes:
# Idea: Sort both lists (O(nlogn)) and then use the 2 pointer method (one pointer for each list).  Start
# from the beginning of each list, and compare the values at each pointer. Total runtime is O(nlogn) with
# a space of O(n).
#
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you 
# cannot load all elements into the memory at once?

from typing import List
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    intersection = []
    pt1 = 0
    pt2 = 0
    while(pt1 < len(nums1) and pt2 < len(nums2)):
        if(nums1[pt1] < nums2[pt2]):
            pt1 += 1
        elif(nums1[pt1] > nums2[pt2]):
            pt2 += 1
        else:
            intersection.append(nums1[pt1])
            pt1 += 1
            pt2 += 1
    return intersection


print(intersect([1],[2]))
