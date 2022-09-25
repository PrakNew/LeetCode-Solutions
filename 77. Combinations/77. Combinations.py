class Solution:
    def combine(self, n, k):
        
        def util(index, path):
            if len(path)==k:
                res.append(path)
                return
            
            for i in range(index, n+1):
                util(i+1, path + [i])
        
        res = []
        util(1, [])
        return res