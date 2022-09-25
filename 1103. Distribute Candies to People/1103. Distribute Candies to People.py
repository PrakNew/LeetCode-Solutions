'''
Idea : Binary search to find the maximum number of people to which candies can be distributed.


Time complexity : O(n)
Space complexity: O(1)  excluding the answer array

'''

class Solution:
    def distributeCandies(self, candies, num_people):
        if num_people == 0:
            return []
        
        lo, hi = 1, 10**9
        ppl = 0
        while lo<=hi:
            mid = (lo+hi)>>1
            total = (mid*(mid+1))>>1
            if candies > total:
                lo = mid + 1
            else:
                if total-mid<candies<=total:
                    ppl = mid
                hi = mid-1
        
        res = [0] * num_people
        ct = 1
        for i in range(1, ppl+1):
            if ct < candies:
                res[(i % num_people)-1] += ct
                candies -= ct
            else:
                res[(i % num_people)-1] += candies
            ct += 1
    
        return res
                