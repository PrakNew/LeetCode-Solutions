#always find the even integer index and check if its next element is same or not and make the changes accordingly
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = 2 * ((lo + hi) // 4)
            print(mid)
            if nums[mid] == nums[mid+1]:
                lo = mid+2
            else:
                hi = mid
        return nums[lo]
        return Counter(nums).most_common()[-1][0]