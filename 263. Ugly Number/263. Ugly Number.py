class Solution:
    def isUgly(self, num):
        if num == 0:
            return False
        if num == 1:
            return True 
        
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        
        return num==1