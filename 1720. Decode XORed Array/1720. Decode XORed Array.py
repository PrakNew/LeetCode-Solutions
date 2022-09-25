"""
Idea: Properties of XOR

Time complexity : O(n)
Space complexity: O(n)
"""

class Solution:
    def decode(self, encoded, first):
        res = [first]
        prev = first
        for ele in encoded:
            last = ele ^ prev
            res.append(last)
            prev = last
        
        return res