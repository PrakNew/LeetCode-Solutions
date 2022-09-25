'''
Time complexity: O(n)
Space complexity: O(n)
'''
import collections

class Solution:
    def subarraySum(self, nums, k):
        
        n = len(nums)
        res = 0
        seen = collections.defaultdict(int)
        seen[0] = 1
        curr_sum = 0
        
        for i in range(n):
            curr_sum += nums[i]
            res += seen[curr_sum - k]
            seen[curr_sum] += 1 
        
        return res
        