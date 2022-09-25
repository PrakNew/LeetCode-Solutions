class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n < 2:
            return n
        
        res = 0
        
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            while b != 0:
                a = a % b
                a, b = b, a
                
            return a
        

        for x in points:
            mp = {}
            dups = 0
            ct = 0
            for y in points:
                if x != y:
                    if x[0] == y[0]:    
                        slope = "inf"
                    else:
                        nr, dr = (y[1] - x[1]), (y[0] - x[0])
                        g = gcd(nr, dr)
                        slope = (nr/g, dr/g)
                    mp[slope] = mp.get(slope, 0) + 1
                    ct = max(ct, mp[slope])
                    
                else:
                    dups += 1
            
            res = max(res, dups + ct)
        
        return res
        