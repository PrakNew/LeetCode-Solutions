class Solution:
    def searchRange(self, A, target):
        
        start, end = -1, -1
        n = len(A)
        
        l = 0
        r = n-1
        
        
        while l<=r:
            mid = (l+r)//2

            if A[mid]==target and (mid==0 or A[mid-1]!=A[mid]):
                start = mid
                break
            
            elif A[mid] >= target:
                r = mid-1
            
            else:
                l = mid+1
        
        l = 0
        r = len(A)-1
        
        while l<=r:
            mid = (l+r)//2
            
            if A[mid]==target and (mid==n-1 or A[mid+1]!=A[mid]):
                end = mid
                break
            
            elif A[mid] > target:
                r = mid-1
            
            else:
                l = mid+1

        
        return [start, end]
        