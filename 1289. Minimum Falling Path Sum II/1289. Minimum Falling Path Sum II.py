class Solution:
    def minFallingPathSum(self, A):
        n = len(A)
        first = A[0][::]
        
        for i in range(1, n):
            second = A[i][::]
            for j in range(n):
                candidates = first[:j] + first[j+1:]
                second[j] += min(candidates)
            first = second[::]

        return min(first)
        