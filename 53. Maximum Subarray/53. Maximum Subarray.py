class Solution:
    def maxSubArray(self, nums) :
        # Kadane's algorithm 
        max_so_far = -float('inf')
        max_here = 0
        for num in nums:
            max_here += num
            max_so_far = max(max_so_far, max_here)
            max_here = max(0, max_here)
        
        return max_so_far