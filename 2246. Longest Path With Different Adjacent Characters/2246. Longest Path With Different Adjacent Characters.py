#simple implementation of DFS
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.c=1
        d=defaultdict(list)
        for end,start in enumerate(parent):
            d[start].append(end)
        visited=set()
        #print(d)
        def dfs(n):
            c1=1
            visited.add(n)
            for x in d[n]:
                if x not in visited:
                    c2=dfs(x)
                    if s[x]!=s[n]:
                        self.c=max(self.c,c2+c1)
                        c1=max(c1,c2+1)
            return c1
        dfs(0)
        return self.c