class Solution:
    def reverseBits(self, n):
        return sum(2**(31-i) for i in range(32) if n & (1<<i))