"""
Idea: Maximum sum subarray problem

Time complexity : O(n)
Space complexity: O(n)
"""

class Solution:
    def minOperations(self, nums, x):
        n = len(nums)
        target = sum(nums) - x
        
        if target == 0:
            return n
        
        # maximum sum subarray with given target
        seen = {0:-1}
        curr_sum = 0
        res = float('-inf')
        for i in range(n):
            curr_sum += nums[i]
            if curr_sum - target in seen:
                res = max(res, i - seen[curr_sum - target])
            seen[curr_sum] = i
        
        return n - res if res > float('-inf') else -1
        
        
        