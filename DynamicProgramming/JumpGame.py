    def reachable(self, index, nums, target):
        #print("looking at index ",index)
        if(index == target):
            return True
        if(nums[index] == 0):
            return False
        for i in range(1,min(nums[index],target-index)+1):
            result = self.reachable(index+i,nums,target)
            print(result)
            if(result == True):
                return True
        return False
    def canJump(self, nums: List[int]) -> bool:
        if(len(nums) == 1):
            return True
        return self.reachable(0,nums,len(nums)-1)