# In order to understand the code you first need to go throught the Decode ways medium level question.
# I am attaching my link to the solution there once you understand that problem you would easily understand this one too.
# Decode Ways
# Click on the above link

# if you have understood the above solution then in below if we use DP we will end up in memory limit exceeded so in order to understand like what needs to be done we just need to modify it to 3 variables as in the below code and use the same logic but instead if * comes first then mulitiply by 9 and similar cases lik 1* means 18 and 2* means 6 and ** means 15 on similar basis you can also solve this problem

class Solution:
    def numDecodings(self, s: str) -> int:
        def decodes_ways(s):
            dp = [0]*(10)
            dp[0] = 1

            if s[0]=='*':
                dp[1] = 9
            elif s[0]!='0':
                dp[1] = 1
            two,one=dp[0],dp[1]
            new=0
            for i in range(2,len(s)+1):
                new=0
                # think about 1-1 chars
                if s[i-1] == '*':
                    new = 9*one
                    if s[i-2]=='1':
                        new += 9*two
                    elif s[i-2] == '2':
                        new += 6*two
                    elif s[i-2] == '*':
                        new += (9*two + 6*two)
                elif s[i-1] !='0':
                    new += one

                # think about 2-2 chars
                if s[i-1]!='*':
                    if s[i-2] == '1' or ( s[i-2] == '2' and s[i-1] < '7' ):
                        new += two
                    elif s[i-2]=='*':
                        new += 2*two if s[i-1]<'7' else two
                two,one=one,new
            return new%(10**9+7)
        return decodes_ways(s)


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
                