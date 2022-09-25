import heapq

class KthLargest:

    def __init__(self, k, A):
        self.pool = A
        self.k = k
        heapq.heapify(A)
        while len(self.pool) > k:
            heapq.heappop(A)
            

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val) 
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)