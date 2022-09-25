class Solution:
    def numIslands(self, grid):
        if grid==[]:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        islands = 0
        
        for x in range(m):
            for y in range(n):
                if not visited[x][y] and grid[x][y]=='1':
                    dfs = [(x, y)]
                    islands += 1
                
                    while dfs:
                        a, b = dfs.pop()
                        visited[a][b] = True
                        
                        for i, j in ((a+1, b), (a-1, b), (a, b+1), (a, b-1)):
                            if 0<=i<m and 0<=j<n and not visited[i][j] and grid[i][j]=='1':
                                dfs.append((i, j))
                
        return islands