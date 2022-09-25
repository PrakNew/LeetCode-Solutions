class Solution:
    def isValid(self, s):
        stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if ch==')' and stack and stack[-1]=='(':
                    stack.pop()
                elif ch=='}' and stack and stack[-1]=='{':
                    stack.pop()
                elif ch==']' and stack and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
        
        return stack==[]
            