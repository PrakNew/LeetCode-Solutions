from heapq import heappush, heappop

class Solution:
    def medianSlidingWindow(self, A, k):
        # 1. Insert k elements into small and move k-k//2 from small to large
        # 2. Ensure len(large) - len(small) <= 1
        # 3. Larger is always non-empty
        
        def move(h1, h2):
            x, ind = heappop(h1)
            heappush(h2, (-x, ind))
        
        def getMedian(h1, h2):
            if k&1:
                return h1[0][0] * 1.
            return (h1[0][0] - h2[0][0]) * 0.5
        
        n = len(A)
        large, small, res = [], [], []
        
        for i in range(k):
            heappush(small, (-A[i], i))
        
        for _ in range(k-(k>>1)):
            move(small, large)
        
        res.append(getMedian(large, small))
        
        for i, x in enumerate(A[k:]):
            if x >= large[0][0]:
                heappush(large, (x, i+k))
                if A[i] <= large[0][0]:
                    move(large, small)
            else:
                heappush(small, (-x, i+k))
                if A[i] >= large[0][0]:
                    move(small, large)
            while small and small[0][1] <= i:
                heappop(small)
            while large and large[0][1] <= i:
                heappop(large)
                
            res.append(getMedian(large, small))
        
        return res