#Link: https://leetcode.com/problems/house-robber/

# 
# Runtime: O(n)
# Space: O(n)
def rob(self, nums: List[int]) -> int:
    if(len(nums) == 0):
        return 0
    elif(len(nums) == 1):
        return nums[0]
    elif(len(nums) == 2):
        return max(nums[0],nums[1])
    else:
        for i in range(2,len(nums)):
            nums[i] = nums[i] + max(nums[0:i-1])
        return max(nums)