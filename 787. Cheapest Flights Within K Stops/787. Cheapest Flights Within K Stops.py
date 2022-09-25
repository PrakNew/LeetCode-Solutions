import collections
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(collections.defaultdict)
        for u, v, w in flights:
            graph[u][v] = w
        heap = [(0, src, K+1)] 
        while heap:
            price, node, k = heapq.heappop(heap) # to get the cheapest flight at every step
            
            if node==dst:
                return price
            
            if k>0:
                for nei in graph[node]:
                    item = (price + graph[node][nei], nei, k-1)
                    heapq.heappush(heap, item)
        
        return -1