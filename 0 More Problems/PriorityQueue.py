import numpy as np
import heapq

l = [1,5,2,3,4]
heap = []
for i in l:
    heapq.heappush(heap, i)
print(heap)