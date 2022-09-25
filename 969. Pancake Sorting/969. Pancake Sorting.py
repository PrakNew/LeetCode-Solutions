class Solution:
    def pancakeSort(self, A):
        def flip(A, k):
            i = 0
            while i < (k>>1):
                A[i], A[k-i-1] = A[k-i-1], A[i]
                i += 1
        
        element_to_sort = len(A)
        res = []
        
        while element_to_sort > 0:
            index = A.index(element_to_sort)
            
            # Make the element go to first position
            if index != element_to_sort - 1:
                if index != 0:
                    res += index + 1,
                    flip(A, index+1)

                # Make the element go to its final position
                res += element_to_sort,
                flip(A, element_to_sort)
            
            element_to_sort -= 1
        
        return res
                