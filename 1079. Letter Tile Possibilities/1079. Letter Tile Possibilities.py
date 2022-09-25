class Solution:
    def numTilePossibilities(self, tiles):
        
        def dfs(A):
            res = 0
            for i in range(26):
                if A[i]>0:
                    res += 1
                    A[i] -= 1
                    res += dfs(A)
                    A[i] += 1
            
            return res
        
        mp = [0] * 26
        for ch in tiles:
            mp[ord(ch) - ord('A')] += 1
        
        return dfs(mp)