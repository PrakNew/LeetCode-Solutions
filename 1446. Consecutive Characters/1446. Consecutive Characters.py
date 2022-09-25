class Solution:
    def maxPower(self, s):
        power = 1
        res = 1
        n = len(s)
        i = 1
        while i < n:
            if s[i]==s[i-1]:
                power+=1
                res = max(res, power)
            else:
                power = 1
            i+=1
        
        return res
        