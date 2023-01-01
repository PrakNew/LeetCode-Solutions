#Good question to understand backtracking
class Solution:
    def uniquePathsIII(self, G: List[List[int]]) -> int:
        M, N, t, z = len(G), len(G[0]), [0], 0
        for i,j in itertools.product(range(M),range(N)):
            if G[i][j] == 0: z += 1
            if G[i][j] == 1: a,b = i,j
            if G[i][j] == 2: e,f = i,j
        G[a][b] = 0
        def dfs(i,j,c):
            if (i,j) == (e,f): t[0] += (c == z+1)
            if G[i][j]: return
            G[i][j] = -1
            for x,y in (i-1,j),(i,j+1),(i+1,j),(i,j-1): 0<=x<M and 0<=y<N and dfs(x,y,c+1)
            G[i][j] = 0
        dfs(a,b,0)
        return t[0]

class Solution:
    def uniquePathsIII(self, grid):
        
        def util(x, y, count):
            count -= 1
            
            if count < 0:
                return 
            
            if (x, y)==(ex, ey):
                if count==0:
                    self.res += 1
                return
            
            grid[x][y] = 3
            
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0<=i<m and 0<=j<n and grid[i][j] in [0, 2]:
                    util(i, j, count)
            
            # backtrack
            grid[x][y] = 0
            
        
        m, n = len(grid), len(grid[0])
        count = 0
        sx, sy = None, None
        ex, ey = None, None
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=-1:
                    count+=1
                if grid[i][j]==1:
                    sx, sy = i, j
                elif grid[i][j]==2:
                    ex, ey = i, j
        
        
        self.res = 0
        util(sx, sy, count)
        return self.res