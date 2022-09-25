class Solution:
    def maxProfit(self, A):
        res = 0
        for i in range(1, len(A)):
            res += (A[i]-A[i-1]) if A[i] > A[i-1] else 0
        
        return res
        