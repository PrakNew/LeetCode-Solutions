"""
Time complexity : O(n)
Space complexity: O(n)
"""

import collections

class Solution:
    def validateStackSequences(self, pushed, popped):
        n, m = len(pushed), len(popped)
        stack = collections.deque()
        i = j = 0

        while i < n and j < m:
            while i < n and (not stack or stack[-1] != popped[j]):
                stack += pushed[i],
                i += 1

            if i == n or j == m:
                break

            stack.pop()
            j += 1

        while j < m:
            if not stack or stack[-1] != popped[j]:
                return False
            stack.pop()
            j += 1

        return True





