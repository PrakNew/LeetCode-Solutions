"""
Idea: Mono stack

Time complexity : O(m*n)
Space complexity: O(n)
"""

import collections

class Solution:
    def maximalRectangle(self, A):
        if not A or not A[0]:   return 0
        m, n = len(A), len(A[0])
        h = [0] * (n+1)
        max_area = 0
        
        for row in A:
            for i in range(n):
                h[i] = h[i] + 1 if row[i] == '1' else 0
                        
            st = collections.deque([-1])
            for i in range(n+1):
                while st and h[st[-1]] > h[i]:
                    height = h[st.pop()]
                    width = i - st[-1] - 1
                    max_area = max(max_area, height * width)   
                st += i,
        
        return max_area