class Solution:
    def maxProfit(self, prices):
        
        # Recurrence relation
        # dp[k][i] = max(dp[k][i-1], prices[i] - prices[j] + dp[k-1][j-1]) j -> 0 to i-1
        
        def dp():
            K = 2
            n = len(prices)
            if n==0:
                return 0

            dp = [[0 for _ in range(n+1)] for _ in range(K+1)]

            for k in range(1, K+1):
                price_j = prices[0]
                for i in range(1, n):
                    price_j = min(price_j, prices[i] - dp[k-1][i-1])
                    dp[k][i] = max(dp[k][i-1], prices[i] - price_j)


            return dp[K][n-1]
        
        
        
        def constantSpace():
            buy1, buy2 = float('inf'), float('inf')
            sell1, sell2, = 0, 0
            
            for price in prices:
                buy1 = min(buy1, price)
                sell1 = max(sell1, price - buy1)
                buy2 = min(buy2, price - sell1)
                sell2 = max(sell2, price - buy2)
            
            return sell2
        
        return constantSpace()