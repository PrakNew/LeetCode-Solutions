"""
Time complexity : O(n)
Space complexity: O(max(levels))
"""

class Solution:
    def lengthLongestPath(self, input):
        res = 0
        system = input.split('\n')
        pathlen = {0: 0}
        
        for level in system:
            name = level.lstrip('\t')
            depth = len(level) - len(name)
            if '.' in name: # a file 
                curr_pathlen = pathlen[depth] + len(name)
                res = max(res, curr_pathlen)
            else:
                pathlen[depth+1] = pathlen[depth] + len(name) + 1
        
        return res
                
                
        
        