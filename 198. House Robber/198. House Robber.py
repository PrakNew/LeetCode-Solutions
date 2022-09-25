class Solution:
    def rob(self, A):
        
        def topDown():
            def rob(i, robbed, n, dp):
                if i>=n:
                    return robbed

                key = (i, robbed)
                if key not in dp:
                    dp[key] = max(rob(i+1, robbed, n, dp), rob(i+2, robbed + A[i], n, dp))
                return dp[key]
            
            n = len(A)
            return rob(0, 0, n, {})
        
        
        def bottomUp(): 
            n = len(A)
            
            if n <= 2:
                return max(A) if n>0 else 0
        
            max_one, max_two = 0, 0
            res = 0
            for i in range(n):
                curr = max(max_two + A[i], max_one)
                max_two = max_one
                max_one = curr
            
            return curr
            

        return bottomUp()

            