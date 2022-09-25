class Solution:
    def maxAreaOfIsland(self, grid):
        
        if grid==[]:
            return 0   
        
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(51)] for _ in range(51)]
        max_area = 0
        
        for r in range(m):
            for c in range(n):
                
                if grid[r][c]==1:
                    
                    path = set()
                    dfs = [(r, c)]
                    
                    while dfs:
                        x, y = dfs.pop()
                        visited[x][y] = True
                        path.add((x, y))

                        for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                            if 0<=i<m and 0<=j<n and not visited[i][j] and grid[i][j]==1:
                                dfs.append((i, j))
                                
                    max_area = max(max_area, len(path))
                                   
        return max_area
        