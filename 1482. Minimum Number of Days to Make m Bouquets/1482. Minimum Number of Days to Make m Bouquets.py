class Solution:
    def minDays(self, A, m, k):
        
        if m*k > len(A): 
            return -1
        
        n = len(A)
        
        def check(day):
            total = 0
            ct = 0
            for a in A:
                if a<=day:
                    ct += 1
                    if ct==k:
                        total+=1
                        ct = 0
                else:
                    ct = 0
            return total >= m
        
        lo = min(A)
        hi = max(A)
        
        while lo<=hi:
            mid = (lo+hi)//2
            if check(mid):
                hi = mid-1
            else:
                lo = mid+1
        
        return lo
        
                
        