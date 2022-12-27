#Easy greedy approach 
class Solution:
    def maximumBags(self, c: List[int], r: List[int], ad: int) -> int:
        for ind in range(len(c)):
            c[ind]-=r[ind]
        c.sort()
        final=0
        for x in c:
            if x==0:
                final+=1
            elif x<=ad:
                final+=1
                ad-=x
            else:
                break
        return final