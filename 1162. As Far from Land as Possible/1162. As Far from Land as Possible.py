class Solution:
    def maxDistance(self, grid):
        res = -1
        m, n = len(grid), len(grid[0])
        found = False
        land_dist = [[-1 for _ in range(n)] for _ in range(m)]
        visited = set()
        q = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    q.add((r, c, 0))
                    visited.add((r, c))
        
        res = -1
        while q:
            temp = set()
            for x, y, dist in q:
                visited.add((x, y))
                if land_dist[x][y]==-1:
                    land_dist[x][y]=dist
                else:
                    land_dist[x][y]=min(land_dist[x][y], dist)

                for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0<=i<m and 0<=j<n and (i, j) not in visited and grid[i][j]==0:
                        found = True
                        temp.add((i, j, dist+1))
            q = temp
                
        res = 0
        for i in range(m):
            res = max(res, max(land_dist[i]))
            
        if res == 0:
            return -1
        
        return res