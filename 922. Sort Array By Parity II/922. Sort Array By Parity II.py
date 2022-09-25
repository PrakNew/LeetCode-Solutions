class Solution:
    def sortArrayByParityII(self, A):
        n = len(A)
        j = 1
        
        for i in range(0, n, 2):
            if A[i] & 1: # odd
                while A[j] & 1: # until you find even
                    j += 2
                A[i], A[j] = A[j], A[i]
                
        return A
        