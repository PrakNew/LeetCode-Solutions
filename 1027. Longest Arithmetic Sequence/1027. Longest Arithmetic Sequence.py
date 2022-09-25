class Solution:
    def longestArithSeqLength(self, A):
        n = len(A)
        dp = {}
        
        for i in range(n):
            for j in range(i+1, n):
                diff = A[j] - A[i]
                dp[j, diff] = dp.get((i, diff), 1) + 1
        
        return max(dp.values())