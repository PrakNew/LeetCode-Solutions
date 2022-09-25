"""
Idea: Binary Indexed Tree

Time complexity : O(log(m*n))    for any query
Space complexity: O(m * n)
"""

class NumMatrix:

    def __init__(self, A):
        m = self.m = len(A)
        if m == 0:
            return None
        n = self.n = len(A[0])
        self.BIT = [[0 for _ in range(n+1)] for _ in range(m+1)]
        self.A = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.update(i, j, A[i][j])
    
    
    def update(self, row, col, val):
        diff = val - self.A[row + 1][col + 1]
        self.A[row + 1][col + 1] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.BIT[i][j] += diff
                j += (j & -j)
            i += (i & -i)
        
    
    def get(self, row, col):
        res = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                res += self.BIT[i][j]
                j -= (j & -j)
            i -= (i & -i)
        
        return res
    

    def sumRegion(self, row1, col1, row2, col2):
        return self.get(row2, col2) - self.get(row2, col1 - 1) - self.get(row1 - 1, col2) + self.get(row1 - 1, col1 - 1)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)