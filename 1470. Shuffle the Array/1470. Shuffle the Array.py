class Solution:
    def shuffle(self, nums, n):
        res = [None] * (2*n)
        
        j = 0
        i = 0
        while j<n:
            res[i] = nums[j]
            res[i+1] = nums[j+n]
            j += 1
            i += 2
        
        return res