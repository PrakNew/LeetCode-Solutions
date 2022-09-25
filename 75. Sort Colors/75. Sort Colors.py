class Solution:
    def sortColors(self, A):
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, len(A)-1
        # use pointer in the middle for traversing
        
        while one <= two:
            if A[one]==0: # swap it with zero pointer
                A[zero], A[one] = A[one], A[zero]
                one += 1
                zero += 1
            elif A[one]==1:
                one += 1
            else: # swap it with two pointer
                A[one], A[two] = A[two], A[one]
                two -= 1
        
        return A
                
                
                