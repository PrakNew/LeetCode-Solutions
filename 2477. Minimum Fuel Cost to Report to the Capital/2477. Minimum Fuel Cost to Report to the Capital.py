# This is a pattern question which is based on finding the count of children nodes 

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        #ceil(cnt/seats)
        path=defaultdict(list)
        for x,y in roads:
            path[x].append(y)
            path[y].append(x)
        self.ans=0
        def dfs(node,parent,cnt=1):
            for x in path[node]:
                if x==parent:continue
                cnt+= dfs(x,node)
            self.ans+=ceil(cnt/seats) if node else 0
            return cnt
        dfs(0,0)
        return self.ans
