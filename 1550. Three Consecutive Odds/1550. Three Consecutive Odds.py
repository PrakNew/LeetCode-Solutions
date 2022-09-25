'''
Time complexity : O(n)
Space complexity: O(1)
'''

class Solution:
    def threeConsecutiveOdds(self, A):
        res = 0
        ct = 0
        n = len(A)
        for i in range(n):
            if A[i]&1:  ct += 1
            else:   ct = 0
            res = max(res, ct)
        return res >= 3
        
        