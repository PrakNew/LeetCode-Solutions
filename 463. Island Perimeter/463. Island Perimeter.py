import collections

class Solution:
    def islandPerimeter(self, grid):
        def getPerimeter(x, y):
            res = 0
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0<=i<m and 0<=j<n and grid[i][j]==0:
                    res += 1
                elif not 0<=i<m or not 0<=j<n:
                    res += 1
            return res
            
        m, n = len(grid), len(grid[0])
        x, y = -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    x, y = i, j
                    break
        
        perimeter = 0
        q = collections.deque([(x, y)])
        visited = {}
        visited[(x, y)] = 1
        
        while q:
            x, y = q.popleft()
            
            # Calculate and perimeter
            perimeter += getPerimeter(x, y)
            
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0<=i<m and 0<=j<n and (i, j) not in visited and grid[i][j]==1:
                    visited[(i, j)] = 1
                    q.append((i, j))
                    
        
        return perimeter
                    