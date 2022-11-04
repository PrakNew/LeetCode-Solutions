# Doing kind off binary search here and working and swapping 

class Solution:
    def reverseVowels(self, s: str) -> str:
        s1=set('aeiouAEIOU')
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            if s[i] in s1 and s[j] in s1:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] not in s1:
                i+=1
            else:
                j-=1
        return ''.join(s)