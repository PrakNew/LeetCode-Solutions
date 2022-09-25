'''
Idea: Use hashmap to store a sum and its index when its encoutered for the first time. 

Time complexity : O(n)
Space complexity: O(1)
'''

class Solution:
    def maxSubArrayLen(self, A, target):
        mp = {0: -1}
        curr_sum, res = 0, 0
        n = len(A)
        for i in range(n):
            curr_sum += A[i]
            if curr_sum == target:  # Subarray from start to current index
                res = i + 1
            elif (curr_sum - target) in mp:
                res = max(res, i - mp[curr_sum - target])
            
            if curr_sum not in mp:
                mp[curr_sum] = i
        
        return res