from heapq import heappush, heappop

def lastStoneWeight(self, stones: List[int]) -> int:
    heap = []
    for stone in stones:
        heappush(heap, -stone)
    
    while len(heap)>1:
        stone1 = heappop(heap)
        stone2 = heappop(heap)
        new_stone = stone1 - stone2
        if new_stone!=0:
            heappush(heap, new_stone)

    if len(heap)==1:
        return -heap[0]
    return 0
    
    