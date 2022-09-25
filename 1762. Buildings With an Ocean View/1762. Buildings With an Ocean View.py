"""
Idea: Process the buildings from ocean

Time complexity : O(n) 
Space complexity: O(1) excluding the output array
"""

class Solution:
    def findBuildings(self, A):
        n = len(A)
        if n == 0:
            return []
        max_so_far = A[n-1]
        res = [n-1]
        
        for i in range(n-2, -1, -1):
            if A[i] > max_so_far:
                res += i,
            max_so_far = max(max_so_far, A[i])
        
        return res[::-1]
        