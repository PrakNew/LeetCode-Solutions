#BFS Implementation
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = [(0,0,k,0)]
        visited = set()
        while queue:
            i, j, chances, count = queue.pop(0)
            tup = (i, j, chances)
            if tup in visited:
                continue
            visited.add(tup)
            if i==n-1 and j==m-1:
                return count
            for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0<=x<n and 0<=y<m and (chances-grid[x][y])>=0:
                    queue.append((x,y,chances-grid[x][y], count+1))
        return -1 