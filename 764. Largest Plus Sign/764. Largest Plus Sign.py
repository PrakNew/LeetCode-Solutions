class Solution:
    def orderOfLargestPlusSign(self, n, mines):
        mines = {tuple(mine) for mine in mines}
        dp = [[0 for _ in range(n)] for _ in range(n)]
        res = 0
        
        for i in range(n):
    
            # left dimension
            ct = 0
            for j in range(n): 
                ct = 0 if (i, j) in mines else ct+1
                dp[i][j] = ct
            
            # right dimension
            ct = 0
            for j in range(n-1, -1, -1): 
                ct = 0 if (i, j) in mines else ct+1
                dp[i][j] = ct if ct < dp[i][j] else dp[i][j]
            
        for j in range(n):
            
            # top dimension
            ct = 0
            for i in range(n):
                ct = 0 if (i, j) in mines else ct+1
                dp[i][j] = ct if ct < dp[i][j] else dp[i][j]
            
            # bottom dimension
            ct = 0
            for i in range(n-1, -1, -1):
                ct = 0 if (i, j) in mines else ct+1
                dp[i][j] = ct if ct < dp[i][j] else dp[i][j]
                if dp[i][j] > res:
                    res = dp[i][j]
            
        return res