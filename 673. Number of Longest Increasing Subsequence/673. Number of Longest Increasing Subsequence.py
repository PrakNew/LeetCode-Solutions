class Solution:
    def findNumberOfLIS(self, A):
        if not A:
            return 0
        
        n = len(A)
        dp = [1] * n
        count = [1] * n 
        
        for i in range(n):
            for j in range(i):
                if A[j] < A[i]:
                    if dp[j] == dp[i]:
                        dp[i] = dp[j]+1
                        count[i] = count[j]
                    elif 1+dp[j] == dp[i]:
                        count[i]+=count[j]
            
        
        maxlen = max(dp)
        res = 0
        for i in range(n):
            if dp[i] == maxlen:
                res += count[i]
        
        return res
        
                    