class Solution:
    def hIndex(self, A):
        
        if A==[]:
            return 0
        
        def getCitations(x):
            i, j = 0, n-1
            while i<j:
                mi = (i+j)>>1
                if A[mi] < x:
                    i = mi + 1
                else:
                    j = mi
            return n-i
                    
        n = len(A)
        l = 0
        r = max(A)
        
        while l<=r:
            mid = (l+r)>>1           
            citations_mid = getCitations(mid)
            citations_mid_1 = getCitations(mid+1)
            if  citations_mid >= mid and citations_mid_1 < (mid+1):
                return mid
            if mid <= citations_mid:
                l = mid + 1
            else:
                r = mid
        
        return l-1