#Simple pattern based question

class Solution:
    def breakPalindrome(self, p: str) -> str:
        if len(p)==1:return ""
        l=list(p)
        for x in range(len(l)//2):
            if l[x]!='a':
                l[x]='a'
                return ''.join(l)
        l[-1]='b'
        return ''.join(l)