"""
Idea: Use Dijkstra's algorithm to find the path with minimum effort. 

Time complexity : O(E log V)
Space complexity: O(EV)

where E = 4 * M * N and V = M * N
"""

import heapq

class Solution:
    def minimumEffortPath(self, A):
        m, n = len(A), len(A[0])
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        q = [(0, 0, 0)]
        
        while q:
            val, x, y = heapq.heappop(q)
            
            if val > dist[x][y]:
                continue 
                
            if (x, y) == (m-1, n-1):
                return val
            
            for i, j in ((x-1, y), (x+1, y), (x, y+1), (x, y-1)):
                if 0<=i<m and 0<=j<n:
                    new_val = max(val, abs(A[i][j] - A[x][y]))
                    if new_val < dist[i][j]:
                        dist[i][j] = new_val
                        heapq.heappush(q, (new_val, i, j))
    
        
        