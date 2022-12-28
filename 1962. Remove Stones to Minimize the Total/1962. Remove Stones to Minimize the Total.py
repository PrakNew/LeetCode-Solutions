# Direct implementation of heapq
import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i]=-piles[i]
        heapq.heapify(piles)
       # print(piles)
        for _ in range(k):
            q=abs(heapq.heappop(piles))
            q=ceil(q/2)
            heapq.heappush(piles,-q)
        return -sum(piles)