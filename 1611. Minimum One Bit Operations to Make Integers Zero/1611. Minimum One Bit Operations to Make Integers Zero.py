class Solution:
    def minimumOneBitOperations(self, n):
        output = 0
        while n>0:
            output ^= n
            n >>= 1
        
        return output
    
        