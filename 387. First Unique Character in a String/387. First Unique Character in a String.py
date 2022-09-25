'''
Time complexity : O(n)
Space complexity: O(1)
'''

import collections

class Solution:
    def firstUniqChar(self, s):
        counter = collections.Counter(s)
        
        for ch in counter:
            if counter[ch]==1:
                return s.index(ch)
        
        return -1
            