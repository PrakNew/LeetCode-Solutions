class Solution:
    def minFallingPathSum(self, A):
        
        def bottomUp():
            m, n = len(A), len(A[0])
            dp = [x[::] for x in A]
            
            for i in range(1, m):
                for j in range(n):
                    left = dp[i-1][j-1] if j>0 else float('inf')
                    top = dp[i-1][j]
                    right = dp[i-1][j+1] if j<n-1 else float('inf')
                    dp[i][j] += min(left, top, right)
    
            return min(dp[m-1])
        
        
        def topDown():
            m, n = len(A), len(A[0])
            dp = [x[::] for x in A]
            
            for i in range(m-2, -1, -1):
                for j in range(n):
                    left = dp[i+1][j-1] if j>0 else float('inf')
                    top = dp[i+1][j]
                    right = dp[i+1][j+1] if j<n-1 else float('inf')
                    dp[i][j] += min(left, top, right)
            
            return min(dp[0])
        
        def linearSpace():
            m, n = len(A), len(A[0])
            first = A[0][::]
            
            for i in range(1, m):
                second = A[i][::]
                for j in range(n):
                    left = first[j-1] if j>0 else float('inf')
                    top = first[j]
                    right = first[j+1] if j<n-1 else float('inf')
                    second[j] += min(left, top, right)
                first = second[::]
        
            return min(first)
        
        return linearSpace()
        return bottomUp()
        return topDown()
        