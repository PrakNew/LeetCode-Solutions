class Solution:
    def findAnagrams(self, s, p):
        
        mask_p = [0]*26
        mask_s = [0]*26
        res = []
        
        for ch in p:
            mask_p[ord(ch)-ord('a')]+=1
        
        for ch in s[:len(p)]:
            mask_s[ord(ch)-ord('a')]+=1

        if mask_s==mask_p:
            res.append(0)

        for i in range(1, len(s)-len(p)+1):
            mask_s[ord(s[i-1])-ord('a')] -= 1
            mask_s[ord(s[i+len(p)-1])-ord('a')] += 1
            
            if mask_s==mask_p:
                res.append(i)
        
        return res