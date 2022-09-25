"""
Idea: Application of stack

Time complexity : O(n)
Space complexity: O(n)
"""

class Solution:
    def asteroidCollision(self, asteroids):
        n = len(asteroids)
        stack = []
        for new in asteroids:
            while stack and new < 0 < stack[-1]:
                if stack[-1] < -new:
                    stack.pop()
                    continue
                elif stack[-1] == -new:
                    stack.pop()
                break
            else:
                stack += new,
        
        return stack
                