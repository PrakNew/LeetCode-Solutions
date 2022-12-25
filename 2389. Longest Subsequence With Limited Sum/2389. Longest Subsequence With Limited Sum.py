#direct implementation question 
import bisect
from itertools import accumulate 
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        l=list(accumulate(nums))
        return [bisect.bisect_right(l,x) for x in queries]