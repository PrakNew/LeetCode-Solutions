import random

class Solution:

    def __init__(self, w):
        self.w = w
        self.n = len(w)
        total = sum(self.w)
        
        for i in range(self.n):
            self.w[i] /= total
        for i in range(1, self.n):
            self.w[i] += self.w[i-1]
        

    def pickIndex(self):
        N = random.uniform(0, 1)
        l = 0
        r = self.n-1
        
        while l<=r:
            mid = (l+r)//2
            if self.w[mid]>=N and (mid==0 or self.w[mid-1] < N):
                return mid
            elif self.w[mid]>N:
                r = mid - 1
            else:
                l = mid + 1
        
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()