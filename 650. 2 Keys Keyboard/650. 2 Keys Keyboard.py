class Solution:
    def minSteps(self, n: int):
        
        if n<=1:
            return 0
        
        def topDown(notepad, clipboard):  
            nonlocal dp
            
            if notepad > n:
                return float('inf')
            
            if notepad==n:
                return 0
        
            if dp[notepad][clipboard] != -1:
                return dp[notepad][clipboard]
            
            copy = topDown(notepad + notepad, notepad) + 2
            paste = topDown(notepad + clipboard, clipboard) + 1
            dp[notepad][clipboard] = min(copy, paste)

            return dp[notepad][clipboard]
        
        
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return 1 + topDown(1, 1)
    