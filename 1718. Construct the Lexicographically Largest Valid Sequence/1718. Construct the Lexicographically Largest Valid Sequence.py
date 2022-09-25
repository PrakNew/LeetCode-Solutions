"""
Idea: Backtracking

Time complexity: O(n!)
Space complexity: O(n)
"""

class Solution:
    def constructDistancedSequence(self, n):
        res = [0] * ((n-1) * 2 + 1)
        seen = {i: False for i in range(1, n+1)}
        
        def dfs(i, res, seen):
            if i == len(res):   # filled all numbers
                return True
            
            if res[i] != 0:     # spot already filled, go to next index
                return dfs(i+1, res, seen)
            
            for j in range(n, 0, -1):
                if seen[j]: # number already filled
                    continue 
                if j != 1 and (i+j >= len(res)  or res[i+j] != 0):     # not able to fill second occurence
                    continue
                
                seen[j] = True
                res[i] = j
                if j > 1:
                    res[i+j] = j
                
                if dfs(i+1, res, seen): # recur for next index
                    return True
                
                # backtrack
                seen[j] = False
                res[i] = 0
                if j > 1:
                    res[i+j] = 0
            
            return False
                
                
        dfs(0, res, seen)
        return res