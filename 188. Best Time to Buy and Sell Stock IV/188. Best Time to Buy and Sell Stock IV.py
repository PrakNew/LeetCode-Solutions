class Solution:
    def maxProfit(self, K, prices):
        n = len(prices)
        if n==0:
            return 0
        
        if K > n>>1: # DP give TLE
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            return res
        
        dp = [[0 for _ in range(n+1)] for _ in range(K+1)]
        for k in range(1, K+1):
            buy = prices[0]
            for i in range(1, n):
                buy = min(buy, prices[i] - dp[k-1][i-1])
                dp[k][i] = max(dp[k][i-1], prices[i] - buy)
        
        return dp[K][n-1]
        