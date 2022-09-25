class Solution:
    def lastStoneWeightII(self, A):
        
        def assign(i, path):
            nonlocal dp
            
            if i==len(A):
                return path if path >= 0 else float('inf')
            
            key = (i, path)
            
            if key not in dp:
                dp[key] = min(assign(i+1, path + A[i]), assign(i+1, path - A[i]))
            
            return dp[key]
            
        dp = {}
        return assign(0, 0)
        
        