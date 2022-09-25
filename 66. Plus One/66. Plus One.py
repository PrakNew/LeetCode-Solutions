class Solution:
    def plusOne(self, digits):
        
        carry = 0
        
        n = len(digits)
        
        i = n-1
        
        digits[i] += 1 
        carry = digits[i]//10
        digits[i] = digits[i] % 10
        i-=1
        
        while carry==1 and i>=0:
            digits[i] += 1 
            carry = digits[i]//10
            digits[i] = digits[i] % 10
            i-=1
        
        if carry==1:
            digits = [1] + digits
        
        
        return digits
            
            