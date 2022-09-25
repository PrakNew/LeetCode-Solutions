"""
Time complexity : O(n!)
Space complexity: O(n!)
"""

class Solution:
    def combinationSum2(self, A, target):
        n = len(A)
        res = []
        
        def util(index, rem, path, res):
            
            if rem < 0:
                return 
            
            if rem == 0:
                path.sort()
                if path not in res:
                    res += path,
                return 
            
            
            for i in range(index, n):
                util(i+1, rem - A[i], path + [A[i]], res)
        
        
        util(0, target, [], res)
        return res
        