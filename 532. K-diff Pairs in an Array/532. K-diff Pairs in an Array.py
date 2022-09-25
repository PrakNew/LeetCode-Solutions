"""
Idea: Since we want unique pairs, on encountering 'x' check if 'x+k' exists in map 

Time complexity : O(n)
Space complexity: O(n)
"""
import collections

class Solution:
    def findPairs(self, A, k):
        mp = collections.Counter(A)
        res = 0
        for x in mp:
            if (k==0 and mp[x] >= 2) or (k>0 and x+k in mp):
                res += 1
        
        return res
        