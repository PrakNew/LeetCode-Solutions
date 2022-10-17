from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d=Counter(nums)
        return sum(key for key, val in d.items() if val==1)