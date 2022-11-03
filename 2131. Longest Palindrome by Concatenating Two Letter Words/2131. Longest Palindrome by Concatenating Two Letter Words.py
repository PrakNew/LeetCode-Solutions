# easy pattern solution where a pattern of characters is theer
from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d=Counter(words)
        c=0
        flag=0
        for x in d:
            rev=x[::-1]
            if x!=rev and d[rev] !=0:
                c+=min(d[x],d[rev])*len(x)
            elif x==rev:
                if flag==0:
                    if d[x] % 2 != 0:
                        flag=1
                    c+=d[x]*len(x)
                else:
                    c += d[x]*len(x) if d[x]%2==0 else (d[x]-1)*len(x)
        return c