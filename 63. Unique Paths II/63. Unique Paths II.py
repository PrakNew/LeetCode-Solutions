class Solution:
    def uniquePathsWithObstacles(self, grid):
        
        if grid==[]:
            return 0
        
        m, n = len(grid), len(grid[0])
        T = [[0 for _ in range(n)] for _ in range(m)]
        

        if grid[0][0]!=1:
            T[0][0] = 1
        
        # first col
        for i in range(1, m):
            if grid[i][0]!=1:
                T[i][0] += T[i-1][0]
        
        # first row
        for j in range(1, n):
            if grid[0][j]!=1:
                T[0][j] += T[0][j-1]
        
        
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j]!=1:
                    T[i][j] = T[i-1][j] + T[i][j-1]
            
        return T[-1][-1]
            