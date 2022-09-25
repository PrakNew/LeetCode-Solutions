"""
Time complexity : O(n)
Space complexity: O(n)
"""

class Solution:
    def getMaximumGenerated(self, n):
        
        if n == 0 or n == 1:
            return n 
        
        dp = [0] * (n+1)
        dp[0], dp[1] = 0, 1
        
        for i in range(2, n+1):
            if i & 1:
                dp[i] = dp[i>>1] + dp[(i>>1) + 1]
            else: 
                dp[i] = dp[i>>1]
        
        return max(dp)