#Easy pattern solution
from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d=Counter(tasks)
        d1={0:0,1:1,2:1,3:1,4:2,5:2}
        c=0
        print(d)
        for x in d:
            if d[x] in d1 and d[x]==1:
                return -1
            if d[x] in d1:
                c+=d1[d[x]]
            else:
                c+=2*(d[x]//6)
                per=d[x]%6
                c+=d1[per]
        return c