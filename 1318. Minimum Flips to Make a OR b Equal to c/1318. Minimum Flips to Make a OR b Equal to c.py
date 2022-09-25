class Solution:
    def minFlips(self, a, b, c):
        res = 0 
        for i in range(32):
            bit_a, bit_b, bit_c = False, False, False
            if a & (1<<i):
                bit_a = True
            if b & (1<<i):
                bit_b = True
            if c & (1<<i):
                bit_c = True
            
            if bit_c == False:
                if bit_a and bit_b:
                    res+=2
                elif bit_a or bit_b:
                    res+=1
            else:
                if bit_a == False and bit_b == False:
                    res+=1
                    
        return res