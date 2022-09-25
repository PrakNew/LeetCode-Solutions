"""
Idea: Greedy

Time complexity : O(n)
Space complexity: O(1)
"""

class Solution:
    def getSmallestString(self, n, k):
        s = ['a'] * n
        k -= n
        i = n - 1
        while k > 0:
            ct = min(k, 25)
            s[i] = chr(97 + ct)
            k -= ct
            i -= 1
        
        return ''.join(s)