
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


import collections

class Solution:
    def shortestPath(self, A, k):
        
        m, n = len(A), len(A[0])
        q = collections.deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])
        
        while q:
            x, y, rem, steps = q.popleft()
            
            if rem < 0:
                continue
            
            if A[x][y]==1:
                rem -= 1
            
            if (x, y) == (m-1, n-1):
                return steps
            
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0<=i<m and 0<=j<n and (i, j, rem) not in visited:
                    visited.add((i, j, rem))
                    q.append((i, j, rem, steps+1))
                    
        return -1
        
                    
                
        