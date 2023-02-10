# Direct BFS implementation 
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n=len(grid)
        queue=[]
        visited=set()
        for x,y in itertools.product(range(n),range(n)):
            if grid[x][y]:
                visited.add((x,y))
                queue.append([x,y,0])
        final=0
        while queue:
            x1,y1,cnt=queue.pop(0)
            final=max(final,cnt)
            for x2,y2 in {(x1+1,y1),(x1-1,y1),(x1,y1+1),(x1,y1-1)}:
                if 0<=x2<n and 0<=y2<n and (x2,y2) not in visited:
                    visited.add((x2,y2))
                    queue.append([x2,y2,cnt+1])

        return final or -1

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