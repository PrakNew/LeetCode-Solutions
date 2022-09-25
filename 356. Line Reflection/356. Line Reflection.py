"""
Idea: Mirror is the median of x-coordinate values

Time complexity : O(n log n)
Space complexity: O(n)
"""

class Solution:
    def isReflected(self, points):
        n = len(points)
        mp = {}
        x_coord = set([x for x, y in points])
        x_coord = list(x_coord)
        x_coord.sort()
  
        mp = {}
        for x, y in points:
            mp[float(x), float(y)] = True
        
        k = len(x_coord)
        mirror = x_coord[k>>1] if k & 1 else (x_coord[k>>1] + x_coord[(k>>1) - 1])/2
  

        for x, y in points:
            if x < mirror:
                reflection = mirror + (mirror - x), y
            else:
                reflection = mirror - (x - mirror), y 
            
            if reflection not in mp:
                print(reflection)
                return False
        
        return True