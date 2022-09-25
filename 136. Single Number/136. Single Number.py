'''
Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def singleNumber(self, A):
        res = 0 
        for a in A:
            res ^= a
        
        return res