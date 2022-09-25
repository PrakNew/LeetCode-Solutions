class Solution:
    def minCostII(self, cost): # n x 3 matrix
        n, k = len(cost), len(cost[0])

        def fn(i, n, prev_house = 0):
            if i==n:
                return 0 
            
            key = (i, prev_house)

            if key not in dp:
                res = float('inf')
                for j in range(1, k+1):
                    if prev_house!=j:
                        res = min(res, cost[i][j-1] + fn(i+1, n, j))
                
                dp[key] = res 
            
            return dp[key]
        
        dp = {}
        return fn(0, n)
