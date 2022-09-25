'''
Time complexity : O(m*n*max(m,n))
Space complexity: O(m*n)
'''

import collections

class Solution:
    def shortestDistance(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        visited = [[float('inf') for _ in range(n)] for _ in range(m)]
        q = collections.deque()
        q += (start[0], start[1]),
        visited[start[0]][start[1]] = 0
        while q:
            x, y = q.popleft()
            for move_x, move_y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r = x + move_x
                c = y + move_y 
                ct = 0
                while 0<=r<m and 0<=c<n and maze[r][c]==0:
                    r += move_x
                    c += move_y
                    ct += 1
                    
                # hit a wall, take a step back
                r -= move_x
                c -= move_y 
                
                if visited[x][y] + ct < visited[r][c] :
                    visited[r][c] = visited[x][y] + ct
                    q += (r, c),
        
        res = visited[destination[0]][destination[1]]
        return res if res<float('inf') else -1