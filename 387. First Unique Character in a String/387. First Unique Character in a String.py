'''
Time complexity : O(n)
Space complexity: O(1)
'''

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=Counter(s)
        return next((i for i, x in enumerate(s) if d[x]==1), -1)

import collections

class Solution:
    def firstUniqChar(self, s):
        counter = collections.Counter(s)
        
        for ch in counter:
            if counter[ch]==1:
                return s.index(ch)
        
        return -1
            