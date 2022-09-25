class Solution:
    def transpose(self, A):
        m, n = len(A), len(A[0])
        T = [[None for _ in range(m)] for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                T[j][i] = A[i][j]
        
        return T