class Solution:
    def coinChange(self, coins, amount):
        
        def topDown():
            n = len(coins)
            count = [0 for _ in range(amount)]
            
            def fn(target):
                if target==0:
                    return 0 # valid
                if target<0:
                    return -1 # invalid
                if count[target-1]:
                    return count[target-1]
                min_ct = float('inf')
                for coin in coins:
                    res = fn(target-coin)
                    if 0<=res<min_ct:
                        min_ct = 1 + res
                        
                count[target-1] = min_ct if min_ct < float('inf') else -1
                return count[target-1]
            
            return fn(amount)
        
        def bottomUp():
            n = len(coins)
            dp = [float('inf')] * (amount+1)
            dp[0] = 0 # valid solution
            
            for coin in coins:
                for amt in range(coin, amount+1):
                    dp[amt] = min(dp[amt], dp[amt-coin]+1)
            
            return dp[amount] if dp[amount] < float('inf') else -1
                
            
        return bottomUp()
        return topDown()
        