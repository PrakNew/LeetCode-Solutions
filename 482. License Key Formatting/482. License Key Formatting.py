"""
Time complexity : O(n)
Space complexity: O(n)
"""
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=''.join(s.split('-')).upper()
        l=[]
        print(s)
        for x in range(len(s)-k,-k,-k):
            l=[s[max(x,0):x+k]]+l
        return '-'.join(l)

class Solution:
    def licenseKeyFormatting(self, S, K):
        chars = []
        for ch in S:
            if 'a' <= ch <= 'z':
                chars += chr(ord(ch) & ord('_')),
            elif 'A' <= ch <= 'Z':
                chars += ch,
            elif ch != '-':
                chars += ch,

        if chars == []:
            return ""

        res = []
        j = 0
        for i in range(len(chars) - 1, -1, -1):
            res += chars[i],
            j += 1
            if j == K:
                res += '-',
                j = 0

        if res[-1] == '-':
            res = res[:-1]
        res = res[::-1]
        return ''.join(res)