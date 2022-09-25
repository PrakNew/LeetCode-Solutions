class Solution:
    def combinationSum3(self, k, n) :
        
        def util(start, target, path, res):
            if target < 0:
                return
            
            if target==0:
                if len(path)==k:
                    res.append(path)
                return
            
            for i in range(start, 10):
                util(i+1, target - i, path + [i], res)
        
        res = []
        util(1, n, [], res)
        return res