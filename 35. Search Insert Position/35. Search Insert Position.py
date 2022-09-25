class Solution:
    def searchInsert(self, A, target):
        lo = 0
        hi = len(A)-1
        
        while lo<hi:
            mid = (lo+hi)//2
            if A[mid]==target:
                return mid
            if A[mid]>target and (mid==0 or A[mid-1]<target):
                return mid
            elif A[mid]<target:
                lo = mid+1
            else:
                hi = mid
        
        if target > A[-1]:
            return len(A)
        return lo
                