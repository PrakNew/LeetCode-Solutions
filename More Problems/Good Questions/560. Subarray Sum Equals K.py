#Algorithm bases question where prefix sum is calculated and then whole lot of it

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        d=defaultdict(int)
        d[0]=1
        p=0
        for x in nums:
            p+=x
           
            if (p-k) in d:
                c+=d[p-k]
            d[p]+=1
        return c