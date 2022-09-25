"""
Idea: Stack

Time complexity : O(n)
Space complexity: O(k)
"""

import collections

class Solution:
    def mostCompetitive(self, A, k):
        n = len(A)
        stack = collections.deque()
        
        for i, x in enumerate(A):
            while stack and x < stack[-1] and (len(stack) - 1 + n - i >= k):
                stack.pop()
            if len(stack) < k:
                stack += x,
        
        return list(stack)