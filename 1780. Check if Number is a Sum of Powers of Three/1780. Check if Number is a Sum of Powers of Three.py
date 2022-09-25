"""
Time complexity : O(log n)
Space complexity: O(1)
"""

class Solution:
    def checkPowersOfThree(self, n):
        
        while n > 1 and n % 3 != 2:
            if n % 3 == 0:
                n //= 3
            else:
                n -= 1
        
        return n == 1
        
                
        