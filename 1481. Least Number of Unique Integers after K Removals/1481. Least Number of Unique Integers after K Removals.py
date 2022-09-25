import collections

class Solution:
    def findLeastNumOfUniqueInts(self, A, k):
        counter = collections.Counter(A)
        freq = []
        for key, val in counter.items():
            freq += [val, key],
        
        freq.sort()
        ct = k
        res = 0
        for val, key in freq:
            if ct==0:
                res += 1
            elif val > ct:
                res += 1
            elif ct >= val:
                ct -= val
            
        return res