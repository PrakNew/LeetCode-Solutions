class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d1=defaultdict(list)
        for x,y,dist in flights:
            d1[x].append((y,dist))
        self.visited={}
        def dfs(n,k1):
            if n==dst:
                return 0
            if (n,k1) in self.visited:
                return self.visited[(n,k1)]
            if k1>k:
                return float("inf")
            distance=float("inf")
            for y,dist in d1[n]:
                distance=min(distance,dfs(y,k1+1)+dist) 
            self.visited[(n,k1)]=distance
            #print(self.visited)
            return distance
        final=dfs(src,0)
        # print(self.visited)
        return final if final!=float("inf") else -1           