class Solution:
    def totalHammingDistance(self, A):
        n = len(A)
        total = 0
        for i in range(32):
            setBits = 0
            for num in A:
                if num & (1<<i): # ith bit set
                    setBits += 1
            total += setBits * (n - setBits)
        
        return total
            