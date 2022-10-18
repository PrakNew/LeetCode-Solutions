#pattern based question 

class Solution:
    def countAndSay(self, n: int) -> str:
        def check(s):
            s=str(s)
            f=''
            prev=s[0]
            count=1
            for x in range(1,len(s)):
                if s[x]==prev:
                    count+=1
                else:
                    f+=str(count)+prev
                    count=1
                    prev=s[x]
            f+=str(count)+prev
            return f
        s='1'
        for x in range(2,n+1):
            s=check(s)
        return s
        