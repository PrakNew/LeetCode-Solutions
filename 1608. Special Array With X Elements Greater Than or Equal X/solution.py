from bisect import bisect_left
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        final=-1
        for x in range(1,n+1):
            ind=bisect_left(nums,x)
            greater = n-ind
            if x==greater:
                final=x
        return final
            