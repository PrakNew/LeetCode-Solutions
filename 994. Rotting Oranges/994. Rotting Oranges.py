import collections

class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        q = collections.deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited[i][j] = True
        ct = None
        res = 0
        while q:
            x, y, ct = q.popleft()
            res = max(res, ct)       
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0<=i<m and 0<=j<n and not visited[i][j] and grid[i][j]==1:
                    q.append((i, j, ct+1))
                    visited[i][j] = True
                    fresh -= 1
        
        return res if fresh==0 else -1