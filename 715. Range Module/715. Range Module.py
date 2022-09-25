"""
Idea: Bisect left and right

Time complexity : O(n), O(log n), O(n) [Add, Query, Remove]
Space complexity: O(n)
"""

from bisect import bisect_left as bl, bisect_right as br


class RangeModule:

    def __init__(self):
        self.X = []        

    def addRange(self, left: int, right: int) -> None:
        i, j = bl(self.X, left), br(self.X, right)
        # succeeding odd-index -> no overlaps -> add the new range
        self.X[i:j] = [left]*(i&1==0) + [right]*(j&1==0)
        

    def queryRange(self, left: int, right: int) -> bool:
        # be conservative -> eg. query [15, 20) in range [10, 15)
        i, j = br(self.X, left), bl(self.X, right)
        # i and j should be equal, should overlap -> succeed even index
        return i == j and i & 1
        

    def removeRange(self, left: int, right: int) -> None:
        i, j = bl(self.X, left), br(self.X, right)
        # succeeding even-index -> overlaps -> remove the range
        self.X[i:j] = [left]*(i&1) + [right]*(j&1)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)