class Solution:
    def wordBreak(self, s, wordDict):
        
        # check if it is breakable
        def wordBreakI():
            n = len(s)
            dp = [False] * n
            for i in range(n):
                for word in wordDict:
                    if s[i-len(word)+1:i+1] == word and (dp[i-len(word)] or i-len(word)==-1):
                        dp[i] = True
            return dp[-1]
        
        
        def wordBreakII(ind, curr, path, res):
            if ind==len(s):
                if curr == '':
                    res += ' '.join(path),
                return
            
            curr += s[ind]
            if curr in wordDict:
                wordBreakII(ind+1, '', path + [curr], res)
            wordBreakII(ind+1, curr, path, res)
        

        
        if not wordBreakI():
            return []
        
        res = []
        wordBreakII(0, '', [], res)
        return res
            
                
        