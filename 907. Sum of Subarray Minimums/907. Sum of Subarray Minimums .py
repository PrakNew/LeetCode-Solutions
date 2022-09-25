"""
Idea: Combine NLE and PLE

Time complexity: O(n)
Space complexity: O(n)
"""

import collections

class Solution:
    def sumSubarrayMins(self, A):
        n = len(A)
        mod = 10**9 + 7
        right = [n - i for i in range(n)]
        left = [i + 1 for i in range(n)]
        
        st = collections.deque()
        # PLE
        for i in range(n):
            while st and A[st[-1]] > A[i]:
                st.pop()
            
            left[i] = i - st[-1] if st else i + 1
            st += i,  
        
        # NLE
        st = collections.deque()
        for i in range(n):
            while st and A[st[-1]] > A[i]:
                right[st[-1]] = i - st[-1]
                st.pop()
            st += i,
        
        res = 0
        for i in range(n):
            res = (res + A[i] * left[i] * right[i]) % mod
        
        return res
  