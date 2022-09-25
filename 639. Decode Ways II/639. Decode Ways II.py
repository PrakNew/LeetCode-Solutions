class Solution:
    def numDecodings(self, s):
        n = len(s)
    
        def fn(i, n):
            if i==n:
                return 1
            
            if i not in dp:
                one_ch, two_ch = 0, 0
                
                if s[i]=='*': 
                    one_ch = 9 * fn(i+1, n)
                    if i+1<n:
                        if s[i+1].isdigit(): # XX
                            if 0<=int(s[i+1])<=6: # 10-16 or 20-26
                                two_ch = 2 * fn(i+2, n)
                            elif 7<=int(s[i+1])<=9: # 17, 18 or 19
                                two_ch = fn(i+2, n)
                        else: # **
                            two_ch = 15 * fn(i+2, n)
        
                    
                elif 1<=int(s[i])<=9: 
                    one_ch = fn(i+1, n)
                    if i+1<n:
                        if s[i+1].isdigit():
                            if 1<=(int(s[i])*10 + int(s[i+1]))<=26:
                                two_ch = fn(i+2, n)
                        else: # s[i+1] is '*'
                            if int(s[i])==1: # 10 - 19
                                two_ch = 9 * fn(i+2, n)
                            elif int(s[i])==2:  # 2*
                                two_ch = 6 * fn(i+2, n)
                
                dp[i] = one_ch + two_ch
            
            return dp[i] % 1000000007
        
        dp = {}
        return fn(0, n)
                