'''
Idea: Have a running product and two pointers to keep track of subarray with product less than K.  
      Update the result in every iteration. 
      Number of subarrays is equal to difference between the two pointers.

Time complexity : O(n)
Space complexity: O(1)
'''

class Solution:
    def numSubarrayProductLessThanK(self, A, target):
        n = len(A)
        curr_prod = 1
        res = 0
        i = 0
        for j in range(n):
            curr_prod *= A[j]
            while i<=j and curr_prod >= target:
                curr_prod /= A[i]
                i += 1
            res += (j-i+1)
        return res
        