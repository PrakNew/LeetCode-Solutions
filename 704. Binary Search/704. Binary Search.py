class Solution:
    def search(self, A, target):
        lo, hi = 0, len(A)-1
        
        while lo<=hi:
            mid = (lo+hi)>>1
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
        
        return -1
        