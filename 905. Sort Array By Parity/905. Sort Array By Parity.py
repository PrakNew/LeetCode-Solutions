class Solution:
    def sortArrayByParity(self, A):
        i = 0
        j = 0
        n = len(A)
        
        while i < n and j < n:
            if A[j] & 1 == 0: # even
                A[i], A[j] = A[j], A[i]
                i+=1
            j+=1
        
        return A
        