class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n<=1:
            return 0
        
        cooldown = [0] * n
        buy = [0] * n
        sell = [0] * n
        
        cooldown[0] = 0
        buy[0] = -prices[0]
        sell[0] = float('-inf')
        
        for i in range(1, n):
            cooldown[i] = max(cooldown[i-1], sell[i-1])
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]) # not buying or buying current stock
            sell[i] = buy[i-1] + prices[i]
        
        return max(cooldown[-1], sell[-1])