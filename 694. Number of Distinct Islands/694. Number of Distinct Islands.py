import collections

class Solution:
    def numDistinctIslands(self, grid):
        if len(grid)==0:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        keys = collections.defaultdict()
        for x in range(m):
            for y in range(n):
                if not visited[x][y] and grid[x][y]==1:
                    q = collections.deque([(x, y)])
                    visited[x][y] = True
                    island_key = []
                    while q:
                        r, c = q.popleft()
                        for i, j in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                            if 0<=i<m and 0<=j<n and not visited[i][j] and grid[i][j]==1:
                                island_key.append((x-i, y-j))
                                q.append((i, j))
                                visited[i][j] = True
                    keys[tuple(island_key)] = 1
        
        return len(keys)
        