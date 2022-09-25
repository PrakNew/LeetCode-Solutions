class Solution:
    def getLastMoment(self, n, left, right):
        
        res = 0
        for ant in left:
            res = max(res, ant)
        
        for ant in right:
            res = max(res, n-ant)
        
        return res
        
        
            