"""
Time complexity: O(m+n)
Space complexity: O(1)
"""
import collections 

class Solution:
    def minCharacters(self, a, b):
        m, n = len(a), len(b)
        c1 = collections.Counter(ord(ch) - 97 for ch in a)
        c2 = collections.Counter(ord(ch) - 97 for ch in b)
        res = m + n - max((c1 + c2).values())       # Condition 3
        
        for i in range(25):
            c1[i + 1] += c1[i]
            c2[i + 1] += c2[i]
            res = min(res, (m - c1[i]) + c2[i])     # Condition 1
            res = min(res, (n - c2[i]) + c1[i])     # Condition 2
        
        return res
        