class Solution:
    def findPeakElement(self, A):
        l, r = 0, len(A)-1
        
        while l<=r:
            mid = (l+r)>>1
            if (mid==0 or A[mid-1] < A[mid]) and (mid==r or A[mid]>A[mid+1]):
                return mid
            elif (mid==0 or A[mid-1] < A[mid]):
                l = mid+1
            else:
                r = mid
        
        return -1
                
            
        
        