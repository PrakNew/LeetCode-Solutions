#pattern based question is here
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for x in strs:
            d[tuple(sorted(x))].append(x)
        return list(d.values())

import collections

class Solution:
    def groupAnagrams(self, strs):
        mp = collections.defaultdict(list)
        
        for i in range(len(strs)):
            mask = [0] * 26
            for ch in strs[i]:
                mask[ord(ch)-ord('a')] += 1
            mp[tuple(mask)].append(strs[i])
        
        return mp.values()