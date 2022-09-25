'''
Time complexity : O(m+n)
Space complexity: O(m+n)
'''

def backspaceCompare(S, T):
    stack1 = []
    stack2 = []
    for ch in S:
        if ch!='#':
            stack1.append(ch)
        else:
            if len(stack1)>0:
                stack1.pop()
    
    for ch in T:
        if ch!='#':
            stack2.append(ch)
        else:
            if len(stack2)>0:
                stack2.pop()
    
    return stack1==stack2

S = "ab#c"; T = "ad#c"
print(backspaceCompare(S, T))