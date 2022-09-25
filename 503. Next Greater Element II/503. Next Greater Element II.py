"""
Idea: Mono stack

Time complexity: O(n)
Space complexity: O(n)
"""

import collections

class Solution:
    def nextGreaterElements(self, A):
        n = len(A)
        nge = [-1] * n        
        
        st = collections.deque()
        for i in range(2*n):
            while st and -A[st[-1]] > -A[i%n]:
                nge[st[-1]] = A[i%n]
                st.pop()
            
            if i < n:
                st += i,
        
        return nge
       