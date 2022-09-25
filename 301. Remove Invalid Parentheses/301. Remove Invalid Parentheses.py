import collections

class Solution:
    def removeInvalidParentheses(self, s):
        
        def valid(s):
            stack = []
            for ch in s:
                if ch=='(':
                    stack.append(ch)
                elif ch==')':
                    if len(stack)>0 and stack[-1]=='(':
                        stack.pop()
                    else:
                        return False
            return len(stack)==0
                    
        
        q = collections.deque([(s, 0)])
        mindist = float('inf')
        visited = set([s])
        setBracket = set(['(',')'])
        res = []
        
        while q:
            state, ct = q.popleft()
            
            if ct > mindist:
                return res
            
            if valid(state):
                if ct <= mindist:
                    mindist = ct
                    res.append(state)
                
            for i in range(len(state)):
                if state[i] in setBracket:
                    new_state = state[:i]+state[i+1:]
                    if new_state not in visited:
                        visited.add(new_state)
                        q.append((new_state, ct+1))
                    
        return res
            
        
        