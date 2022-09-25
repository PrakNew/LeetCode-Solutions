import collections

class Solution:  
    def canConstruct(self, s: str, k: int) :
        mp = collections.defaultdict()
        for ch in s:
            if ch not in mp:
                mp[ch] = 0
            mp[ch] += 1
        
        odd = 0
        even = 0
        # count # of odd characters
        for ch, freq in mp.items():
            if freq&1==1:
                odd += 1
        
        return odd<=k<=len(s)
            
        