'''
Time complexity: O(n)
Space complexity: O(n)
'''
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        d=defaultdict(int)
        d[0]=1
        p=0
        for x in nums:
            p+=x
           
            if (p-k) in d:
                c+=d[p-k]
            d[p]+=1
        return c

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
        