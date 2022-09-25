"""
Idea: DP

Time complexity: O(m*n log (m*n))
Space complexity: O(m*n)
"""

class Solution:
    def kthLargestValue(self, A, k):
        m, n = len(A), len(A[0])
        xor = [[0 for _ in range(n+1)] for _ in range(m+1)]
        mp = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                xor[i][j] = xor[i-1][j] ^ xor[i][j-1] ^ A[i-1][j-1] ^ xor[i-1][j-1]
                mp += xor[i][j],
            
        mp.sort(reverse = True) 
        
        return mp[k-1]
        
        