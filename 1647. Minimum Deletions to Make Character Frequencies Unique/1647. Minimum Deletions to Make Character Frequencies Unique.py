#We will be using the calculating  the frequencies and deleting the number until it is not in the previous frequencies set
from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        d=Counter(s)
        s=set()
        final=0
        for x in d:
            if d[x] not in s:
                s.add(d[x])
            else:
                while d[x] in s:
                    d[x]-=1
                    final+=1
                if d[x]:s.add(d[x])
        return final