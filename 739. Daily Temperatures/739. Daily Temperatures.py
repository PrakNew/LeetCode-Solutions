# Using Monotonic Stack it was implemented
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        final=[0]*len(temperatures)
        for ind,x in enumerate(temperatures):
            #print(stack)
            if stack != [] and stack[-1][1] < x:
                while stack!=[] and stack[-1][1]<x:
                    top=stack.pop()
                    final[top[0]]=ind-top[0]
            stack.append([ind,x])
        return final


class Solution:
    def dailyTemperatures(self, T):
        n = len(T)
        stack = []
        res = [0] * n
        
        for i in range(n-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
                
            if stack:
                res[i] = stack[-1] - i
                
            stack.append(i)
              
        return res
                
                
                