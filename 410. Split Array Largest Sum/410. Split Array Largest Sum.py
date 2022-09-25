class Solution:
    def splitArray(self, A, m):
        
        def canSplit(target, A, m):
            total = 0
            ct = 1
            for x in A:
                total += x
                if total > target: # end sub array
                    total = x  # start new subarray
                    ct += 1
                    if ct > m:
                        return False
            return True
        
        # binary search between largest element and sum of array
        l = float('-inf')
        r = 0
        for x in A:
            l = x if x > l else l
            r += x
        
        while l<=r:
            mid = (l+r)>>1
            res = canSplit(mid, A, m)
            if res: # possible to split array, try smaller target
                r = mid - 1
            else:
                l = mid + 1
        
        return l