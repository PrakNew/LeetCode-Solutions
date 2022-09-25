class Solution:
    def moveZeroes(self, A):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(A)
        for j in range(n):
            if A[j]:
                A[i], A[j] = A[j], A[i]
                i+=1
        
        return A