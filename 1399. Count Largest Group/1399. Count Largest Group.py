import collections

class Solution:
    def countLargestGroup(self, n):
        mp = collections.defaultdict(list)
        max_size = 0
        
        for num in range(1, n+1):
            sum_dgts = sum([int(i) for i in list(str(num))])
            if sum_dgts not in mp:
                mp[sum_dgts] = []
            mp[sum_dgts].append(num)
            max_size = max(max_size, len(mp[sum_dgts]))
            
        res = 0
        for key, val in mp.items():
            if len(val)==max_size:
                res+=1
        
        return res
        