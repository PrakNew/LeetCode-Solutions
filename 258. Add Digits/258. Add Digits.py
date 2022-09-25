class Solution:
    def addDigits(self, x):
        return 1 + (x-1)%9 if x else 0
        