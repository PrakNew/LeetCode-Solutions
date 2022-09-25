'''
Boyer Moore Voting algorithm

Time complexity : O(n)
Space complexity: O(1)
'''

class Solution:
    def majorityElement(self, nums):
        ct = 0
        candidate = None
        for i in range(len(nums)):
            if ct==0:
                candidate = nums[i]
                
            if nums[i]==candidate:
                ct += 1
            else:
                ct -=1
            
        return candidate