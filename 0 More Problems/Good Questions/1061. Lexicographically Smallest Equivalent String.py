# The question is based on DFS plus I have used the pass by reference feature of list in this

from sortedcontainers import SortedList
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d=defaultdict(list)
        visited=set()
        for x,y in zip(s1,s2):
            d[x].append(y)
            d[y].append(x)
        final={}
        def dfs(x,l):
            if x in visited:return 
            visited.add(x)
            l.add(x)
            final[x]=l
            for q in d[x]:
                dfs(q,l) 
        for x in set(s1)|set(s2):
            if x not in visited:
                dfs(x,SortedList())
        #print(final)
        s=''
        for x in baseStr:
            s+=final.get(x,[x])[0]
        return s 