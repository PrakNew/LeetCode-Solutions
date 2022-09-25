class Solution:
    def change(self, amount, coins):
        res = [0] * (amount+1)
        res[0] = 1
        
        for coin in coins:
            for i in range(1, amount+1):
                if i>=coin:
                    res[i] += res[i-coin]
        
        return res[-1]