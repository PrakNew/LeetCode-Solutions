# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        rand40 = 40
        while rand40 >= 40:
            row, col = rand7(), rand7()
            rand40 = ((row-1) * 7 + col-1)
        return rand40 % 10 + 1
        