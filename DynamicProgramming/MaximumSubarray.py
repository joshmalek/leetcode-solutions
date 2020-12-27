#Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/

def maxSubArray(self, nums: List[int]) -> int:
    local_max = total_max = nums[0]
    for i in range(1,len(nums)):
        local_max = max(nums[i],local_max+nums[i])
        total_max = max(local_max,total_max)
    return total_max