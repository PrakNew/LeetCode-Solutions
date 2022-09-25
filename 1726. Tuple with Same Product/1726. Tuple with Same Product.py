"""
Idea: Maintain a hashmap of products of all distinct numbers.
        If a product is already encountered, increase result by
        8 times frequency, because 4 numbers can be arranged in 8
        different ways.

Time complexity: O(n^2)
Time complexity: O(n^2)
"""

import collections

class Solution:
    def tupleSameProduct(self, nums):
        mp = collections.defaultdict(int)
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i):
                prod = nums[i] * nums[j]
                res += 8 * mp[prod]
                mp[prod] += 1
        
        return res
        