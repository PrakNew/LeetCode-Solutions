class Solution:
    def singleNumber(self, nums):
        bits = [0] * 32
        for num in nums:
            for i in range(32):
                if num & (1<<i):
                    bits[i]+=1
        res = 0
        isNegative = False
        for i in range(32):
            if bits[i] % 3 == 1:
                res += (1<<i)
                if i==31:
                    isNegative = True
        
        if isNegative:
            return res - pow(2, 32)
        
        return res
        
            
                
            