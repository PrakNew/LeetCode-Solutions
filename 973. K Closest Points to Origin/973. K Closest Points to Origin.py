import heapq

class Solution:
    def kClosest(self, points, K) :
        
        heap = [((pt[0]**2 + pt[1]**2), pt) for pt in points] 
        
        heapq.heapify(heap)
        
        return [ heapq.heappop(heap)[1] for _ in range(K)]