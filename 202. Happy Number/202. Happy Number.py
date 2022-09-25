class Solution:
    def isHappy(self, n: int):
        max_iter = 10**2
        ss = 0
        for dgt in list(str(n)):
            ss += int(dgt)**2
        
        while ss!=1:
            n = ss
            ss = 0
            for dgt in list(str(n)):
                ss += int(dgt)**2
            max_iter-=1
            if max_iter==0:
                break
        
        return ss==1