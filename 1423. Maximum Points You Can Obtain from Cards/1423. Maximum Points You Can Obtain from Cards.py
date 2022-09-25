'''
Idea: Answer = Total sum - minimum sum of contiguous subarray of length (n-k)

Time complexity : O(n)
Space complexity: O(1)
'''

class Solution:
    def maxScore(self, A, k):
        n = len(A)
        length = n - k
        minSum = sum(A[0:length])
        res = minSum
        
        for i in range(length, n):
            minSum -= A[i-length]
            minSum += A[i]
            if minSum < res:
                res = minSum
        
        return sum(A) - res
        
            
                