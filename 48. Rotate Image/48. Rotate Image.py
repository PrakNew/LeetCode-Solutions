class Solution:
    def rotate(self, A):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(A), len(A[0])
        
        # swap elements across left diagonal
        for i in range(m):
            for j in range(i+1, n):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        
        for i in range(m):
            print(A[i])
            
        # reverse elements in each row
        for i in range(m):
            for j in range(n>>1):
                A[i][j], A[i][n-j-1] = A[i][n-j-1], A[i][j]
    
        

