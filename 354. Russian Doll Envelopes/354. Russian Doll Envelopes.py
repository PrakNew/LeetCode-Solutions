import bisect

class Solution:
    def maxEnvelopes(self, A):
        A.sort(key = lambda x: (x[0], -x[1]))
        
        h = []
        
        for i, e in enumerate(A):
            j = bisect.bisect_left(h, e[1])
            if j < len(h):
                h[j] = e[1]
            else:
                h.append(e[1])

        return len(h)
        
                
        