class Solution:
    def wordBreak(self, s, wordDict):
        
        def topDown():
            def check(i, j, n):
                if i==n: # A word ended in n-1 position
                    return True
                if j>n:
                    return False
                key = (i, j)
                if key not in dp:
                    # word can either be formed or not formed
                    formed, wait = False, False
                    if s[i:j+1] in wordSet:
                        formed = check(j+1, j+1, n)
                    # wait until it is formed
                    wait = check(i, j+1, n)
                    dp[key] = formed or wait
                return dp[key]
        
            wordSet = set(wordDict)
            dp = {}
            return check(0, 0, len(s))
        
        
        def bottomUp():
            n = len(s)
            dp = [False] * (n+1)
            wordSet = set(wordDict)
            for i in range(n+1):
                for word in wordSet:
                    if s[i-len(word):i] == word and (dp[i-len(word)-1] or (i-len(word)-1)==-1):
                        dp[i-1] = True
            return dp[n-1]
        
        return bottomUp()
        