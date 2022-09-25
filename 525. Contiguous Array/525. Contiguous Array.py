'''
Time complexity : O(n)
Space complexity: O(n)
'''

import collections

class Solution:
    def findMaxLength(self, A):
        res = 0
        mp = collections.defaultdict()
        mp[0] = -1
        curr_sum = 0
        for i, x in enumerate(A):
            curr_sum += 1 if x == 1 else -1
            if curr_sum in mp:
                
                res = max(res, (i - mp[curr_sum]))
            else:
                mp[curr_sum] = i
        
        
        return res
        