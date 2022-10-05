# Simple DFS question with visted set O(N) both 

from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination :return True
        d=defaultdict(lambda : [])
        for x,y in edges:
            d[x].append(y)
            d[y].append(x)
        visited=set()
        def check(x):
            visited.add(x)
            l=d[x]
            if destination in l:
                return True
            for x1 in l:
                if x1 not in visited:
                    x=check(x1)
                    if x:return True
            return False
        return check(source)
        