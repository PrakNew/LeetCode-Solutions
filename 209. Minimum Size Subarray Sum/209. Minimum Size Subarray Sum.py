'''
Time complexity : O(n)
Space complexity: O(1)
'''

class Solution:
    def minSubArrayLen(self, target, A):
        res = float('inf')
        curr_sum = 0
        n = len(A)
        i = 0
        
        for j in range(n):
            curr_sum += A[j]
            
            while i<=j and curr_sum >= target:
                if curr_sum >= target:
                    res = min(res, j-i+1)
                curr_sum -= A[i]
                i += 1
                
        return res if res < float('inf') else 0
            