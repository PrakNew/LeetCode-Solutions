#easy solution
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        l=list(s)
        l.sort(key=lambda x:(d[x],x),reverse=True)
        return ''.join(l)


class Solution:
    def frequencySort(self, s):
        table = set()
        for ch in set(s):
            table.add((s.count(ch), ch))
        
        res = ""
        
        for freq, ch in sorted(table, reverse=True):
            res += ch*freq
        
        return res