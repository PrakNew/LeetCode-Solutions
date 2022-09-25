class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        
        a, b = A, B
        while a:
            a, b = b%a, a
        gcd = b  
        
        lcm = A*B/gcd
        
        lo = min(A, B)
        hi = N*min(A, B)
        
        while lo<hi:
            mid = (lo+hi)//2
            if mid//A + mid//B - mid//lcm < N:
                lo = mid+1
            else:
                hi = mid
        
        return lo % (10**9+7)