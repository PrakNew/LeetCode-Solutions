"""
Idea: Binary Indexed Tree (BIT)

Time complexity: O(n log n) to create the tree
Space complexity: O(log n) to answer queries/update

"""

class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.BIT = [0] * (self.n + 1)
        for i in range(self.n):
            self.update(i + 1, nums[i])
        

    def sumRange(self, i, j):
        x, y = i + 1, j + 1     # BIT follows 1-based indexing
        return self.get(y) - self.get(x-1)
    
    def update(self, index, val):
        while index <= self.n:
            self.BIT[index] += val
            index += (index & (-index))
    
    def get(self, index):
        res = 0
        while index > 0:
            res += self.BIT[index]
            index -= (index & (-index))
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)