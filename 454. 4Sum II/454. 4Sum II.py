class Solution:
    def fourSumCount(self, A, B, C, D):
        mp = {}
        for a in A:
            for b in B:
                if a+b not in mp:
                    mp[a+b] = 0
                mp[a+b] += 1
        res = 0
        for c in C:
            for d in D:
                if -(c+d) in mp:
                    res += mp[-c-d]
        
        return res