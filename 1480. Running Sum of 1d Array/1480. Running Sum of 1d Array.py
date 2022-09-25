class Solution:
    def runningSum(self, nums):
        prefix = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            prefix[i] = nums[i-1] + prefix[i-1]
        
        return prefix[1:]