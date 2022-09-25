"""
Idea: Mono stack and use of NLE/PLE

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def largestRectangleArea(self, A):
        if not A:   return 0
        n = len(A)
        res = 0
        st = [-1]
        h = A[:] + [0]
        for i in range(n + 1):
            while st and h[st[-1]] > h[i]:
                height = h[st.pop()]
                width = i - st[-1] - 1
                res = max(res, height * width)
            st += i,
        
        return res