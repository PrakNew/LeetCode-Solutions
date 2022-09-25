class Solution:
    def isMonotonic(self, A):
        
        n = len(A)
    
        # monotonic increasing 
        if A[0]<=A[n-1]:
            for i in range(1, n):
                if A[i]<A[i-1]:
                    return False
        # monotonic decreasing
        else:
            for i in range(1, n):
                if A[i]>A[i-1]:
                    return False 
        
        return True
        