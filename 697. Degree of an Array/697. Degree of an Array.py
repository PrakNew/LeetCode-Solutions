"""
Idea: Maintain left and right indices for each element. Check the difference between
        left and right indices of elements with highest frequencies.

Time complexity : O(n)
Space complexity: O(n)
"""


import collections

class Solution:
    def findShortestSubArray(self, A):
        mp = collections.defaultdict(int)
        left = collections.defaultdict(int)
        right = collections.defaultdict(int)
        n = len(A)
        max_degree = 0

        for i in range(n):
            
            if A[i] not in mp:
                left[A[i]] = i
                
            mp[A[i]] += 1
            
            if mp[A[i]] >= max_degree:
                max_degree = mp[A[i]]
                
            right[A[i]] = i
        
        res = n
        for x in mp:
            if mp[x] == max_degree:
                res = min(res, right[x] - left[x] + 1)
        
        return res
        
        