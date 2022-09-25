class Solution:
    def validPalindrome(self, s):
        
        def isPalindrome(a):
            return a==a[::-1]
        
        l, r = 0, len(s)-1
        
        while l<r:
            if s[l]!=s[r]:
                return isPalindrome(s[l:r]) or isPalindrome(s[l+1:r+1])
            l+=1
            r-=1
        
        return True