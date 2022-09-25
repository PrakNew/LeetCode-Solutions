class Solution:
    def climbStairs(self, n):
        one, two = 1, 0
        for i in range(1, n+1):
            curr_step = one + two
            two = one
            one = curr_step
        return curr_step