class Solution:
    def hammingDistance(self, x, y):
        z = x ^ y
        # count set bits in z
        setBits = 0
        while z > 0 :
            setBits += 1
            z &= z-1
        
        return setBits
            
            