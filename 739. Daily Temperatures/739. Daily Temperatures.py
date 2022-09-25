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
                
                
                