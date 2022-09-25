'''
Idea: Solve it on paper. Maintain two stacks: one for operators and one for numbers.
      Whenever an operator is encountered, keep popping the top of the stack until the top of stack
     as precedence greater than current operator. On each pop on operator stack, pop two elements from 
     number stack and push the result back onto number stack.

     Order of precedence:
     (, )
     +, -

     Time complexity : O(n)
     Space complexity: O(n)
'''


import collections

class Solution:
    def calculate(self, s):
        
        order = {'(': 2, '+': 1, '-': 1}
        op = collections.deque()
        stack = collections.deque()
        i = 0
        
        while i < len(s):
            
            while i < len(s) and s[i]==" ":
                i += 1
            
            if i < len(s) and s[i] == '(': 
                op.append(s[i])
                i += 1
            
            num = 0
            isNum = False
            while i < len(s) and s[i].isdigit():
                isNum = True
                num *= 10
                num += int(s[i])
                i += 1
            
            if isNum:
                stack.append(num)
                
            if i < len(s) and s[i] in ['+', '-']:
                while op and order[op[-1]] <= order[s[i]]:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    sign = op.pop()
                    if sign == '+':
                        res = num1 + num2
                    else:
                        res = num1 - num2
                    stack.append(res)
                op.append(s[i])
                i += 1
                    
            if i < len(s) and s[i] == ')':
                while op and op[-1] != '(':
                    num2 = stack.pop()
                    num1 = stack.pop()
                    sign = op.pop()
                    if sign == '+':
                        res = num1 + num2
                    else:
                        res = num1 - num2
                    stack.append(res)
                # Pop '(' from op
                op.pop()
                i += 1
    
                
        while op:
            num2 = stack.pop()
            num1 = stack.pop()
            sign = op.pop()
            if sign == '+':
                res = num1 + num2
            else:
                res = num1 - num2
            stack.append(res)
        
    
        return stack[0]
            