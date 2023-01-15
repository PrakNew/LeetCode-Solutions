# The basic logic over here is suppose k is 5 and earlier sum was 2 and after 2 index sum is 7
# so for both 2 and 7 %5 will always be 2 so that means if we can get that 2 has already came earlier
# then one can conclude that the sum between them will always be multiple of k


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: -1}
        s=0
        for i,x in enumerate(nums):
            s+=x
            mod=s%k
            if mod not in d:
                d[mod]=i
            elif i-d[mod]>=2:
                return True
        return False
    