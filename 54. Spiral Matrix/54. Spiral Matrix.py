"""
Idea: Traverse depth wise

Time complexity : O(m*n)
Space complexity: O(1)
"""

class Solution:
    def spiralOrder(self, A):
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2+1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1
                
            
        if not A or not A[0]:
            return []
        
        m, n = len(A), len(A[0])
        res = []
        i, j = 0, 0
        r1, r2 = 0, m-1
        c1, c2 = 0, n-1
        
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                res += A[r][c],
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        
        return res
            