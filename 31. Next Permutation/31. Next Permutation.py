class Solution:
    def nextPermutation(self, A):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(A)
        i = n-2

        # 1. find first decreasing number from right
        while i>=0 and A[i]>=A[i+1]: 
            i-=1
        
        if i>=0:
            # 2. find smallest number larger than A[i]
            j = n-1
            while j>=0 and A[j]<=A[i]:
                j-=1
            # swap A[i], A[j]
            A[i], A[j] = A[j], A[i]
            
            
        # 3. reverse elements from i+1 to N
        l = i+1
        r = n-1
        while l<r:
            A[l], A[r] = A[r], A[l]
            l+=1
            r-=1
            
        