'''
Motivation : To toggle a bit XOR the bit with 1

1 ^ 1 = 0
0 ^ 1 = 1
 
Time complexity : O(log N)
Space complexity: O(1)
'''

class Solution:
    def findComplement(self, num):
        res = 0
        temp = num
        while temp:
            res+=1
            temp //= 2
        
        return (2**(res)-1) ^ num