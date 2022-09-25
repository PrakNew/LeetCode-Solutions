'''
Time complexity : O(n)
Space complexity: O(n)

'''

import collections

class Solution:
    def numJewelsInStones(self, J, S):
        ct = 0
        J = set(J)
        counter = collections.Counter(S)
        for stone in counter:
            if stone in J:
                ct += counter[stone]
        return ct