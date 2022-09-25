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