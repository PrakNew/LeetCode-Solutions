'''
Idea : Converting decimal number to base-26 number

Time complexity :
Space complexity:
'''

class Solution:
    def convertToTitle(self, n):
        res = ''
        while n>0:
            n -= 1
            letter = n%26
            res = chr(ord('A') + letter) + res
            n //= 26
        return res
        