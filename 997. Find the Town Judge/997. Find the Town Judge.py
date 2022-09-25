import collections

class Solution:
    def findJudge(self, N, trust):
        
        if trust == []:
            return 1
        
        mp1 = collections.defaultdict()
        mp2 = set()
        for pair in trust:
            if pair[1] not in mp1:
                mp1[pair[1]]=0
            mp1[pair[1]] += 1
            
            mp2.add(pair[0])
            
        
        for key, val in mp1.items():
            if val == N-1 and key not in mp2:
                return key
           
        return -1