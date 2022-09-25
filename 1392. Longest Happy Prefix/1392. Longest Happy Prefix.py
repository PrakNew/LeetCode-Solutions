def longestPrefix(self, s: str) -> str:
        
        n = len(s)
        ans = ""
        
        for i in range(n):
            prefix = s[:i]
            suffix = s[-i:]
            if prefix==suffix and prefix!=s:
                ans = prefix
        
        return ans