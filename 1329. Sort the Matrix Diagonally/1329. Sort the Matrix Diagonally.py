"""
Idea: Traverse diagonal one by one sorting them

Time complexity : O(m*n)
Space complexity: O(max(m, n))
"""

class Solution:
    def diagonalSort(self, A):
        m, n = len(A), len(A[0])

        for i in range(m):
            x, y = i, 0
            diag = []
            while x < m and y < n:
                diag += A[x][y],
                x += 1
                y += 1
            diag.sort()
            x, y = i, 0
            k = 0
            while x < m and y < n:
                A[x][y] = diag[k]
                x += 1
                y += 1
                k += 1
                

        for j in range(1, n):
            x, y = 0, j
            diag = []
            while x < m and y < n :
                diag += A[x][y],
                x += 1
                y += 1
            diag.sort()
            x, y = 0, j
            k = 0
            while x < m and y < n:
                A[x][y] = diag[k]
                x += 1
                y += 1
                k += 1
        
        return A
                
            
            