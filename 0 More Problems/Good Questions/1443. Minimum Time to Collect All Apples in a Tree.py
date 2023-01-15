# This is a tricky question which states that if we visit a node where there is apple then we have to do ans+2
# and also the trick is we have to do ans+2 for all the parent nodes 

from collections import defaultdict
from typing import List
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        d=defaultdict(list)
        visited = set()
        for x,y in edges:
            d[x].append(y)
            d[y].append(x)
        def dfs(n):
            visited.add(n)
            ans=0
            for x in d[n]:
                if x not in visited:
                    ans+=dfs(x)
            return 0 if ans==0 and hasApple[n]==False else ans+2

        return max(0,dfs(0)-2)