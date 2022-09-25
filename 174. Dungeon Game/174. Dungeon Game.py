class Solution:
    def calculateMinimumHP(self, A):
        m, n = len(A), len(A[0])
        H = [[0 for _ in range(n)] for _ in range(m)]
        
        if A[m-1][n-1] < 0:
            H[m-1][n-1] = abs(A[m-1][n-1]) + 1
        else:
            H[m-1][n-1] = 1
        
        # last column 
        for i in range(m-2, -1, -1):
            H[i][n-1] = max(1, H[i+1][n-1] - A[i][n-1])
        
        # last row
        for j in range(n-2, -1, -1):
            H[m-1][j] = max(1, H[m-1][j+1] - A[m-1][j])
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                H[i][j] = min(H[i+1][j], H[i][j+1]) - A[i][j]
                H[i][j] = max(1, H[i][j])
        
        return H[0][0]