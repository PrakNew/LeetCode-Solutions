class Solution:
    def minAddToMakeValid(self, S):
        res = 0
        stack = []
        for ch in S:
            if ch is '(':
                stack.append(ch)
            elif ch is ')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    res += 1
        
        res += len(stack)
        
        return res