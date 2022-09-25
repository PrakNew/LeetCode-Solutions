"""
Idea: Mono stack

Time complexity: O(n)
Space complexity: O(n)
"""

import collections

class Solution:
    def nextGreaterElement(self, A, B):
        st = collections.deque()
        nge = [-1] * len(B)
        for i in range(len(B)):
            while st and -B[st[-1]] > -B[i]:
                nge[st[-1]] = i
                st.pop()
            st += i,
        
        mp = {}
        for i in range(len(B)):
            mp[B[i]] = B[nge[i]] if nge[i] != -1 else -1
        
        res = []
        for x in A:
            res += mp.get(x, -1),
        
        return res
        
        
