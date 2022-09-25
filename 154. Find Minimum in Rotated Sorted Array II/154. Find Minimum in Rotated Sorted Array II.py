class Solution:
    def findMin(self, A):
        n = len(A)
        l, r = 0, n-1
        
        while l<r:
            mid = (l+r)>>1
            if A[l]==A[mid]==A[r]:
                l+=1
                r-=1
            elif A[mid]<=A[r]:
                r = mid
            else:
                l = mid+1
        
        return A[l]