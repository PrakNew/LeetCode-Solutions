class Solution:
    def findUnsortedSubarray(self, A):
        n = len(A)
        
        # Find the min and max in the unsorted array
        min_elem, max_elem = float('inf'), float('-inf')
        started = False
        for i in range(1, n):
            if A[i] < A[i-1]: # unsorted array has started
                started = True
                if started:
                    min_elem = min(min_elem, A[i])
        
        if not started: # array is sorted
            return 0
        
        started = False
        for i in range(n-2, -1, -1):
            if A[i] > A[i+1]: # unsorted array has started
                started = True
                if started:
                    max_elem = max(max_elem, A[i])
        

        l, r = 0, n-1
        
        # find correct positions of min and max_elem
        for i in range(n):
            if A[i] > min_elem:
                l = i
                break
        
        for i in range(n-1, -1, -1):
            if A[i] < max_elem:
                r = i
                break
        
        return r-l+1