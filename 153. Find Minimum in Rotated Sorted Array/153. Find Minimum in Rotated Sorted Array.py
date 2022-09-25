class Solution:
    def findMin(self, A):
        
        def check(x):
            return (x==0 or A[x-1] > A[x]) and (x==n-1 or A[x+1] > A[x])
            
        n = len(A)
        l, r = 0, n-1
        
        if A[0] < A[-1]:
            return A[0]
        
        while l<=r:
            mid = (l+r)>>1
            
            if check(mid):
                return A[mid]
            
            elif mid<n-1 and check(mid+1):
                return A[mid+1]
            
            elif (A[mid] < A[r]):
                r = mid-1
                
            else:
                l = mid+1
        
        return A[l]