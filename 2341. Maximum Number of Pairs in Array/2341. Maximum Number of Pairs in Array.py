# Brute force question

from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        l=[0,0]
        for x in d:
            if d[x]%2==0:
                l[0]+=d[x]//2
            else:
                l[0]+=d[x]//2
                l[1]+=1
        return l