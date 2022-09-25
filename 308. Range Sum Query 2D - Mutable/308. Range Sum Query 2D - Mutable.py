"""
Idea: Binary Indexed Trees

Time complexity : O(log(m) * log(n)) for each update/search
Space complexity: O(mn)
"""

class NumMatrix:

    def __init__(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        m, n = len(matrix), len(matrix[0])
        self.BIT = [[0 for _ in range(n+1)] for _ in range(m+1)]
        self.A = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        m, n = len(self.A), len(self.A[0]) 
        diff = val - self.A[row][col]
        self.A[row][col] = val
        i = row + 1
        while i <= m:
            j = col + 1
            while j <= n:
                self.BIT[i][j] += diff
                j += (j & (-j))
            i += (i & (-i))        
                

    def sumRegion(self, row1, col1, row2, col2):
        p, q, r, s = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.get(r, s) - self.get(r, q-1) - self.get(p-1, s) + self.get(p-1, q-1)
    
    def get(self, row, col):
        res = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                res += self.BIT[i][j]
                j -= (j & (-j))
            i -= (i & (-i))
        
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)