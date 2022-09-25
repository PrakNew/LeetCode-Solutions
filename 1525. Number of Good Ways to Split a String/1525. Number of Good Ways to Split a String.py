"""
Idea: Sliding window

Time complexity : O(n)
Space complexity: O(n)
"""
import collections

class Solution:
    def numSplits(self, s):
        A = collections.Counter()
        B = collections.Counter(s)
        res = 0
        n = len(s)
        for i in range(n):
            A[s[i]] += 1
            B[s[i]] -= 1
            
            if B[s[i]] == 0:
                del B[s[i]]
                
            if len(A) == len(B):
                res += 1
            
        return res
            