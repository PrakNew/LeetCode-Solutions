class Solution:
    def minimumTotal(self, A):
        
        def bottomUp():
            m = len(A)
            dp = [a[::] for a in A]

            for i in range(1, m):
                prev_n = len(dp[i-1])
                n = len(dp[i])
                for j in range(n):
                    left = dp[i-1][j-1] if j>0 else float('inf')
                    right = dp[i-1][j] if j<prev_n else float('inf')
                    dp[i][j] += min(left, right)

            return min(dp[m-1])
        
        def linearSpace():
            m = len(A)
            first = A[0][::]
            second = None
            prev_n, n = 1, 2
            
            for i in range(1, m):
                second = A[i][::]
                for j in range(n):
                    left = first[j-1] if j>0 else float('inf')
                    right = first[j] if j<prev_n else float('inf')
                    second[j] += min(left, right)
                first = second[::]
                prev_n, n = n, n+1
                
            return min(first)
        
        return linearSpace()