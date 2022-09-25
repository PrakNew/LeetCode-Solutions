class Solution:
    def hIndex(self, citations):
        
        if not citations:
            return 0
        
        def getCitations(h):
            return sum(1 for x in citations if x>=h)
        
        l, r = 0, len(citations)
        candidate = 1
        while l<=r:
            mid = (l+r)>>1
            no_citations = getCitations(mid)
            if no_citations >= mid:
                candidate = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return candidate