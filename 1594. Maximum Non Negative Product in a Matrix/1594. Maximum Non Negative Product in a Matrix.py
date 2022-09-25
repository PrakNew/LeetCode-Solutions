class Solution:
    def maxProductPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        min_prod = [[None for _ in range(n)] for _ in range(m)]
        max_prod = [[None for _ in range(n)] for _ in range(m)]
        
        min_prod[0][0] = max_prod[0][0] = grid[0][0]
        
        for i in range(1, m):
            min_prod[i][0] = max_prod[i][0] = max_prod[i-1][0] * grid[i][0]
        
        for j in range(1, n):
            min_prod[0][j] = max_prod[0][j] = max_prod[0][j-1] * grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] < 0:
                    max_prod[i][j] = min(min_prod[i-1][j], min_prod[i][j-1]) * grid[i][j]
                    min_prod[i][j] = max(max_prod[i-1][j], max_prod[i][j-1]) * grid[i][j]
                else:
                    max_prod[i][j] = max(max_prod[i-1][j], max_prod[i][j-1]) * grid[i][j]
                    min_prod[i][j] = min(min_prod[i-1][j], min_prod[i][j-1]) * grid[i][j]
        
        return max_prod[m-1][n-1] % (pow(10, 9) + 7) if max_prod[m-1][n-1] >=0 else -1


                
        