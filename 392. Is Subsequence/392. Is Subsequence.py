class Solution:
    def isSubsequence(self, s, t):
        m, n = len(t), len(s)
        i = 0
        j = 0
        while i<m and j<n:
            if s[j]==t[i]:
                i+=1
                j+=1
            else:
                i+=1
        
        return j==n