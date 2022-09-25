class Solution:
    def isPerfectSquare(self, num):
        
        lo = 1
        hi = num
        
        if num==1:
            return True
        
        while lo<hi:
            mid = (lo + hi) // 2
            
            if mid*mid == num:
                return True
            
            elif mid*mid > num:
                hi = mid
            
            else:
                lo = mid + 1
        
        return False