class Solution:
    # Gauss formula
    def missingNumber(self, A):
        n = len(A)
        original_sum = n*(n+1)//2
        return original_sum - sum(A)
                