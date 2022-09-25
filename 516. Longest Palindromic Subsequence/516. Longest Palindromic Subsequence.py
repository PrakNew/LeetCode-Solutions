'''
Idea: LPS is LCS of s and its reverse.

Time complexity : O(n^2)
Space complexity: O(n^2)
'''

class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        T = [[0 for _ in range(n+1)] for _ in range(n+1)]
        x, y = s, s[::-1]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if x[i-1]==y[j-1]:
                    T[i][j] = T[i-1][j-1] + 1
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])
        return T[n][n]
    