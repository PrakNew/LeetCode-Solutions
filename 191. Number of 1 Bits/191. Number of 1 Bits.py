class Solution:
    def hammingWeight(self, n):
        ct = 0
        while n>0:
            ct+=1
            n &= (n-1)
        return ct
        