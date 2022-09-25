class Solution:
    def minPathSum(self, A):
        
        def topDown():
            m, n = len(A), len(A[0])
            dp = [[-1 for _ in range(n)] for _ in range(m)]
            
            def fn(i, j):
                if not 0<=i<m or not 0<=j<n:
                    return float('inf')
                
                if dp[i][j]!=-1:
                    return dp[i][j]
                
                if (i, j)==(m-1, n-1): # solution
                    return A[i][j]
                
                dp[i][j] = min(fn(i+1, j), fn(i, j+1)) + A[i][j]
                
                return dp[i][j]
            
            return fn(0, 0)
        
        def bottomUp():
            m, n = len(A), len(A[0])
            dp = [x[::] for x in A]
                        
            # last column
            for i in range(m-2, -1, -1):
                dp[i][n-1] += dp[i+1][n-1]
            # last row
            for j in range(n-2, -1, -1):
                dp[m-1][j] += dp[m-1][j+1]
            
            for i in range(m-2, -1, -1):
                for j in range(n-2, -1, -1):
                    dp[i][j] += min(dp[i+1][j], dp[i][j+1])
            
            return dp[0][0]
        
        
        def linearSpace():
            m, n = len(A), len(A[0])
            top = [0 for _ in range(n)]
            bottom = A[m-1][::]
            
            # last row
            for j in range(n-2, -1, -1):
                bottom[j] += bottom[j+1]
            
            for i in range(m-2, -1, -1):
                top = A[i][::]
                top[-1] += bottom[-1] # last column values
                for j in range(n-2, -1, -1):
                    top[j] += min(top[j+1], bottom[j])
                bottom = top[::]
                
            return bottom[0]
        
        # return topDown()
        # return bottomUp()
        return linearSpace()
        