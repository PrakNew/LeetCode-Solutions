
def checkValidString(s):
    stars = []
    stack = []
    
    for i in range(len(s)):
        ch = s[i]
        if ch=='(':
            stack.append((ch, i))
        elif ch==')':
            if len(stack)>0 and stack[-1][0]=='(':
                stack.pop()
            elif len(stars) > 0:
                stars.pop()
            else:
                return False
        else: # ch is *
            stars += [i]
    
    if not stack:
        return True


    while stack and stars:
        if stack[-1][1] > stars[-1]:
            return False
        else:
            stack.pop()
            stars.pop()
            
    if stack: # not enough stars 
        return False
            
    return True
        
        