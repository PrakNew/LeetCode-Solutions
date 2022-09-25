'''

Since given array is circular the robber cannot steal house[0] and house[n-1] simultaneously. 
Compute the maximum sum subsequence with no adjacent elements for both cases separately and 
return the maximum. 

Time complexity : O(n)
Space complexity: O(1)

'''

class Solution:
    def rob(self, A):
        n = len(A)
        if n<=3:
            return max(A) if n>0 else 0
        
        def topDown():
            n = len(A)
            
            def rob(i, robbed, n, dp):
                if i>=n:
                    return robbed
                
                key = (i, robbed)
                if key not in dp:
                    dp[key] = max(rob(i+2, robbed + A[i], n, dp), rob(i+1, robbed, n, dp))
                
                return dp[key]
            
            return max(rob(0, 0, n-1, {}), rob(1, 0, n, {}))
        
        
        def bottomUp():
            def rob(l, r):
                max_one, max_two = 0, 0
                curr = 0
                for i in range(l, r):
                    curr = max(max_one, max_two + A[i])
                    max_two = max_one
                    max_one = curr
                return curr
            
            return max(rob(0, n-1), rob(1, n))
        
        return bottomUp()
        return topDown()
