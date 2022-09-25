class Solution:
    def removeDuplicateLetters(self, s):
        last = {c: i for i, c in enumerate(s)}
        stack = []
        
        for i, c in enumerate(s):
            if c in stack:
                continue
            
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            
            stack += c,
        
        return ''.join(stack)