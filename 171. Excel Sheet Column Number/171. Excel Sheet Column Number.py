'''
Idea: Converting a base-26 number to decimal form.

Time complexity : O(n)
Space complexity: O(1)
'''

class Solution:
    def titleToNumber(self, s):
        n = len(s)
        res = 0 
        for i in range(n):
            mul = ord(s[i]) - ord('A') + 1
            res += mul * pow(26, n-i-1)
        return res