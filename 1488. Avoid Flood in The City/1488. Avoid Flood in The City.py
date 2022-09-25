import collections, heapq

class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        lake_day = collections.defaultdict(list)
        full = set()
        heap = []
        res = [-1] * n
        for day, lake in enumerate(rains):
            lake_day[lake].append(day)
        
        for i in range(n):
            lake = rains[i]
            if lake:
                if lake in full:
                    return []
                full.add(lake)
                lake_day[lake].pop(0)
                if lake_day[lake]:
                    heapq.heappush(heap, lake_day[lake][0])
                    
            else:
                if heap:
                    day = heapq.heappop(heap)
                    lake = rains[day]
                    res[i] = lake
                    full.remove(lake)
                else:
                    res[i] = 1
        
        return res