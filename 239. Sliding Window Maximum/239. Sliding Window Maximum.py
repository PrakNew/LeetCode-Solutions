import heapq

class Solution:
    def maxSlidingWindow(self, A, k):
        if k==1:
            return A
        n = len(A)
        res = []
        q = []
        for i in range(k):
            heapq.heappush(q, (-A[i], i))
        res.append(-q[0][0])
        
        for i in range(1, n-k+1):
            while q[0][1] <= i-1: # pop until first element is within window [i, i+k-1]
                heapq.heappop(q)
            heapq.heappush(q, (-A[i+k-1], i+k-1))
            res.append(-q[0][0])
        
        return res
        