'''
Idea: Perform BFS starting from (0, 0) covering neighbors step by step. 

'''

import collections

class Solution:
    def minKnightMoves(self, x, y):
        visited = collections.defaultdict()
        visited[(0, 0)] = 1
        q = collections.deque([(0, 0, 0)])
        while q:
            r, c, steps = q.popleft()
            if r==x and c==y:
                return steps
            for i, j in ((r-2, c-1), (r-2, c+1), (r+2, c-1), (r+2, c+1), (r-1, c-2), (r+1, c-2), (r-1, c+2), (r+1, c+2)):
                if (i, j) not in visited:
                    visited[(i, j)] = 1
                    q.append((i, j, steps+1))
                    
        return -1
        