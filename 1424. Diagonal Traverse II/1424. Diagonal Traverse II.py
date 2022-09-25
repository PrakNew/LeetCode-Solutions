'''
Algorithm : Diagonals elements of a matrix hash to same bucket if indices were summed.

Time complexity: O(A)
Space complexity: O(A)
'''

import collections

class Solution:
    def findDiagonalOrder(self, A):
        
        mp = collections.defaultdict(list)
        
        m = len(A)
        
        if m==0:
            return []
        
        for i in range(m):
            for j in range(len(A[i])):
                mp[i+j].append(A[i][j])
        
        res = []
        
        for key, val in mp.items():
            res += val[::-1]
        
        return res