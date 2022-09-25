"""
Time complexity : O(1)
Space complexity: O(n)
"""
import collections 

class MovingAverage:

    def __init__(self, size: int):
        self.arr = collections.deque()
        self.size = size 
        self.curr_sum = 0 
        self.count = 0
        
    def next(self, val: int) -> float:
        if self.count == self.size:
            self.curr_sum -= self.arr.popleft()
            self.count -= 1
        
        self.count += 1
        self.arr += val, 
        self.curr_sum += val 
        return self.curr_sum / self.count
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)