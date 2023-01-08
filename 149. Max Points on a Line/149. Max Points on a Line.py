# Following the slope formulae y=mx + b and finding m,b in the question 
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        def slope(p1,p2):
            if p2[0]-p1[0] == 0:
                return (p1[0])
            slope = (p2[1]-p1[1]) / (p2[0]-p1[0])                
            b = p1[1] - slope * p1[0]
            return (slope,"%.5f" % b)
        d=defaultdict(set)
        for p1,p2 in itertools.product(points,points):
            if p1!=p2:
                slp=slope(p1,p2)
                d[slp].add(tuple(p1))
                d[slp].add(tuple(p2))
        # print(d)
        # print(slope((1,1),(2,1)))
        return len(sorted(d.values(),key=lambda x:len(x))[-1])

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
        