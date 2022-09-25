'''
Time complexity : O(n)
Space complexity: O(1) excluding the result array
'''


class Solution:
    def fizzBuzz(self, n):
        res = []
        for i in range(1, n+1):
            if i%3==0 and i%5==0:
                res += "FizzBuzz",
            elif i%3==0:
                res += "Fizz",
            elif i%5==0:
                res += "Buzz",
            else:
                res += str(i),
        return res