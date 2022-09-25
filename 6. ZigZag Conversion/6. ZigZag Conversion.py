'''
Idea: Rail fence cipher technique.

Time complexity: O(m*n)
Space complexity: O(m*n)
'''

class Solution:
    def convert(self, s, m):
        if m == 1:
            return s
        n = len(s)
        T = [[None for _ in range(n)] for _ in range(m)]
        
        i = j = 0
        k = 0
        
        while k < n:
            while k<n and i<m:
                T[i][j] = s[k]
                i += 1
                k += 1
            
            i = m-2
            j += 1
            while k<n and j<n and i>=0:
                T[i][j] = s[k]
                i -= 1
                j += 1
                k += 1
            
            i = 1
    
    
        res = ''
        for i in range(m):
            for j in range(n):
                if T[i][j]:
                    res += T[i][j]
        
        return res