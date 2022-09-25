import collections

class Solution:
    def minIncrementForUnique(self, A):
        
        taken = []
        count = collections.Counter(A)
        ans = 0
        
        for i in range(50000):
            if count[i]>=2:
                taken.extend([i] * (count[i] - 1))
            elif count[i]==0 and taken:
                ans += i - taken.pop()
        
        return ans