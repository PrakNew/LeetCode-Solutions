"""
Idea: Mono stack

Time complexity: O(n)
Space complexity: O(n)
"""

import collections

class StockSpanner:

    def __init__(self):
        self.st = collections.deque()

    def next(self, price):
        ct = 1
        while self.st and self.st[-1][0] <= price:
            ct += self.st[-1][1]
            self.st.pop()
        
        self.st += (price, ct),
        return ct


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)