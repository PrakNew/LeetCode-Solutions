class NumArray:

    def __init__(self, nums):
        self.n = n = len(nums)
        self.A = nums
        self.BIT = [0] * (n + 1)
        for i in range(n):
            self.updateBIT(i+1, nums[i])

    def update(self, index, val):
        diff = val - self.A[index]
        self.A[index] = val
        self.updateBIT(index + 1, diff)
        

    def sumRange(self, left, right):
        x, y = left + 1, right + 1
        return self.get(y) - self.get(x-1)
    
    def updateBIT(self, index, val):
        n = self.n
        while index <= n:
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
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)