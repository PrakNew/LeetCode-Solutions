"""
Time complexity : O(n^2)
Space complexity: O(n)
"""

class Solution:
    def numberOfBoomerangs(self, points):
        if not points:
            return 0

        res = 0
        for pt1 in points:
            mp = {}
            for pt2 in points:
                x = (pt1[0] - pt2[0])
                y = (pt1[1] - pt2[1]) 
                mp[x*x + y*y] = mp.get(x*x + y*y, 0) + 1
            
            for d in mp:
                res += mp[d] * (mp[d] - 1)
        return res
            
        