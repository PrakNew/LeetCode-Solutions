class Solution:
    def maxCoins(self, nums):
        
        dims = [1] + nums + [1]
        n = len(dims)
        lookup = [[0 for _ in range(n+1)] for _ in range(n+1)]        
        
        def util(i, j, lookup):

            if j<=i+1:
                return 0
            
            maxCost = -float('inf')
            
            if lookup[i][j]==0:
                for k in range(i+1, j):
                    cost = util(i, k, lookup)
                    cost += util(k, j, lookup)
                    cost += dims[i] * dims[k] * dims[j]
                    maxCost = max(maxCost, cost)
                lookup[i][j] = maxCost
            
            return lookup[i][j]
        
        
        return util(0, n-1, lookup)
        