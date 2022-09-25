'''
Time complexity : O(m*n*max(m,n))
Space complexity: O(m*n)
'''


import collections

class Solution:
    def hasPath(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        q = collections.deque([(start[0], start[1])])
        visited[start[0]][start[1]] = True
        while q:
            x, y = q.popleft()
            if (x, y) == (destination[0], destination[1]):
                return True
            for move_x, move_y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r = x + move_x
                c = y + move_y
                
                while 0<=r<m and 0<=c<n and maze[r][c] == 0:
                    r += move_x
                    c += move_y
                
                # hit the wall, so take a step back
                r -= move_x
                c -= move_y
                
                if not visited[r][c]:
                    visited[r][c] = True
                    q += (r, c),
        
        return False
        