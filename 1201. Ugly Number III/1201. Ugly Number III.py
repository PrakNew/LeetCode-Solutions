import math

class Solution:
    def nthUglyNumber(self, n, a, b, c):
    
        def lcm(x, y):
            return x * y // math.gcd(x, y)
        
        
        def countFactors(n):
            ans = n//a + n//b + n//c 
            ans -= (n//ab + n//ac + n//bc)
            ans += n//abc
            return ans
        
        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(ab, c)
        
        l = 1
        r = 2 * 10**9
        
        while l < r:
            mid = (l+r)>>1
            if countFactors(mid) < n:
                l = mid + 1
            else:
                r = mid
        
        return l
    
        