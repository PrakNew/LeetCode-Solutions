class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp = collections.defaultdict()
        
        for num in arr:
            if num not in mp:
                mp[num] = 0
            mp[num] += 1
        
        res = -1
        for key, val in mp.items():
            if key==val and key>res:
                res = key
        
        return res