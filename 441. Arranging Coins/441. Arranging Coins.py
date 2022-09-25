class Solution:
    def arrangeCoins(self, n):
        if n<=1:
            return n
        
        l = 1
        r = n
        res = 0
        while l<r:
            mid = (l+r)>>1
            candidate = (mid * (mid + 1)) >> 1
            if candidate <= n:
                res = mid
                l = mid + 1
            else:
                r = mid 
        
        return res