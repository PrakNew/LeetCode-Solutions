'''
Time complexity : O(n)
Space complexty: O(1)
'''

class Solution:
    def minOperations(self, n):
        res = 0
        num = 1
        if n&1: # odd
            mid = 2 * (n>>1) + 1
            for i in range(n>>1):
                res += (mid-num)
                num += 2
        else: # even
            mid_2 = (2 * (n>>1) + 1)
            mid = (mid_2 * 2 - 2) >> 1
            for i in range(n>>1):
                res += (mid-num)
                num += 2
        return res
        