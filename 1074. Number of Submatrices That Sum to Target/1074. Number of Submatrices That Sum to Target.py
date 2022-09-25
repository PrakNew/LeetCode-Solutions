"""
Time complexity : O(m^2 * n)
Space complexity: O(m * n)
"""

import collections

class Solution:
    def numSubmatrixSumTarget(self, A, target: int) -> int:
        
        m, n = len(A), len(A[0])

        S = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
        # compute the 2D prefix sum
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + A[i-1][j-1] 
        
        res = 0
        for r1 in range(1, m + 1):
            for r2 in range(r1, m + 1):
                mp = collections.defaultdict(int)
                mp[0] = 1
                for col in range(1, n + 1):
                    curr_sum = S[r2][col] - S[r1 - 1][col]
                    res += mp[curr_sum - target]                    
                    mp[curr_sum] += 1
                
        return res                    