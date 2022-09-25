class Solution:
    def minCost(self, houses, cost, m, n, target):
        
        def dfs(index, target, prev_house = None):
            if index >= len(houses) or target < 0:
                if target==0:
                    return 0
                return float('inf')
            
            if houses[index]!=0:
                if prev_house == houses[index]:
                    return dfs(index+1, target, prev_house)
                return dfs(index+1, target-1, houses[index])
            
            key = (index, target, prev_house)
            
            if key not in dp:
                res = float('inf')
                for clr in range(1, n+1):
                    if clr == prev_house:
                        res = min(res, cost[index][clr-1] + dfs(index+1, target, clr))
                    else:
                        res = min(res, cost[index][clr-1] + dfs(index+1, target-1, clr))
                dp[key] = res
            
            return dp[key]
        
        
        dp = {}
        res = dfs(0, target)
        
        if res < float('inf'):
            return res
        return -1
        