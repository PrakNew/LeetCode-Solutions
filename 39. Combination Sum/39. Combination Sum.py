"""
Idea: Backtracking

Time complexity : O(2^n)
Space complexity: O(2^n)
"""

class Solution:
    def combinationSum(self, candidates, target):
        n = len(candidates)
        
        def util(index, rem, path, res):
            if rem == 0:
                res += path,
                return
            
            # Backtrack if necessary
            if rem < 0 or index >= n:
                return
 
            util(index, rem - candidates[index], path + [candidates[index]], res)

            util(index + 1, rem, path, res)
                
                
        dp = {}
        res = []
        util(0, target, [], res)
        return res 