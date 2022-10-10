#Simple pattern based question 


class Solution:
    def myAtoi(self, s: str) -> int:
       
        s=s.strip()
        if not s:return 0
        l=list(s)
        flag='0'
        if l[0] in ['-', '+']:
            flag=l[0]
            del l[0]
        i,j=0,len(l)
        s1='0'
        while i<j and l[i].isdigit():
            s1+=l[i]
            i+=1
        s1=flag+s1
        return max(-2**31,min(2**31-1,int(s1)))