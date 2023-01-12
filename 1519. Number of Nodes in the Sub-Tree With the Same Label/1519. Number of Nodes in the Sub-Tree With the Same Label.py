# Easy implementation based on DFS the only new thing to learn from here is COUNTER adds the values of each keys
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        visited=set()
        d=defaultdict(list)
        for x, y in edges:
            d[x].append(y)
            d[y].append(x)
        self.l=[0]*len(labels)
        def dfs(n):
            visited.add(n)
            d1=Counter()
            d1[labels[n]]+=1
            for x in d[n]:
                if x not in visited:
                    d1+=dfs(x)
            self.l[n]=d1[labels[n]]
            return d1
        dfs(0)
        return self.l
