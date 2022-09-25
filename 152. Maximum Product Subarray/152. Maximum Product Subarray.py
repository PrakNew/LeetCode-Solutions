class Solution:
    def maxProduct(self, A):
        n = len(A)
        maxval, minval = 1, 1
        res = float('-inf')
        
        for i in range(n):
            if A[i] >= 0:
                maxval *= A[i]
                minval *= A[i]
            elif A[i] < 0:
                maxval, minval = minval * A[i], maxval * A[i]
            
            res = max(maxval, res)
            maxval = max(1, maxval)
            minval = min(1, minval)
        
        return res