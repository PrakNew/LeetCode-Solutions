"""
Idea: Two heaps 

Time complexity : O(N log N)
Space complexity: O(N)
"""

import heapq

class Solution:
    def longestSubarray(self, A, limit):
        n = len(A)
        res = 0
        left = 0
        max_heap = []
        min_heap = []
        
        for right in range(n):
            heapq.heappush(max_heap, (-A[right], right))
            heapq.heappush(min_heap, (A[right], right))
            
            while max_heap and max_heap[0][1] < left:
                heapq.heappop(max_heap)
            
            while min_heap and min_heap[0][1] < left:
                heapq.heappop(min_heap)
                
            while left < right and (-max_heap[0][0] - min_heap[0][0]) > limit:
                left += 1
                while max_heap and max_heap[0][1] < left:
                    heapq.heappop(max_heap)

                while min_heap and min_heap[0][1] < left:
                    heapq.heappop(min_heap)
                
            res = max(res, right - left + 1)
        
        return res
