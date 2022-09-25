class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n==0:
            return 0
        
        def dynamicProgramming():
            K = 1
            dp = [[0 for _ in range(n+1)] for _ in range(K+1)]
            for k in range(1, K+1):
                buy = prices[0]
                for i in range(1, n):
                    buy = min(buy, prices[i] - dp[k-1][i-1])
                    dp[k][i] = max(dp[k][i-1], prices[i] - buy)
            return dp[K][n-1]
        
        def constantSpace():
            buy = float('inf')
            sell = float('-inf')
            for i in range(n):
                buy = min(buy, prices[i])
                sell = max(sell, prices[i] - buy)
            return sell if sell > float('-inf') else 0
        
        return dynamicProgramming()\
        return constantSpace()