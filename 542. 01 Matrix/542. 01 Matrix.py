class Solution:
    def updateMatrix(self, A):
        if A==[]:
            return []
        m, n = len(A), len(A[0])
        
        q = []
        
        for i in range(m):
            for j in range(n):
                if A[i][j]==0:
                    q.append([i, j])
                else:
                    A[i][j] = float('inf')
        
        while q:
            x, y = q.pop(0)
            
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0<=i<m and 0<=j<n and A[i][j] > A[x][y] + 1:
                    q.append([i, j])
                    A[i][j] = A[x][y] + 1
        
        return A
            
        