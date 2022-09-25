"""
Idea: DFS using heap

Time complexity : O(RC log RC)
Space complexity: O(RC)
"""

import heapq

class Solution:
    def maximumMinimumPath(self, A):
        res = float('inf')
        R, C = len(A), len(A[0])
        
        heap = [(-A[0][0], 0, 0)]
        visited = [[False for _ in range(C)] for _ in range(R)]
        
        while heap:
            val, x, y = heapq.heappop(heap)
            
            if (x, y) == (R-1, C-1):
                return -val
            
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0<=i<R and 0<=j<C and not visited[i][j]:
                    visited[i][j] = True
                    heapq.heappush(heap, (max(val, -A[i][j]), i, j))
    
        return 0