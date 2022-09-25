class Solution:
    def findTargetSumWays(self, A, S):
        
        def assign(i, path):
            nonlocal dp
            if i == len(A):
                return 1 if path==S else 0
            
            key = (i, path)
            
            if key not in dp:
                dp[key] = assign(i+1, path + A[i]) + assign(i+1, path - A[i])
        
            return dp[key]
        
        dp = {}
        return assign(0, 0)