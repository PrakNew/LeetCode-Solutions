"""
Idea: Hashmap to count the remaining occurences of the each element. Another hashmap to count the
      last elements of each subsequence formed

Time complexity: O(n)
Space complexity: O(n)
"""

import collections

class Solution:
    def isPossible(self, A):
        n = len(A)
        count = collections.Counter(A)
        end = collections.Counter()
        
        for x in A:
            if not count[x]:
                continue
            count[x] -= 1
            if end[x-1] > 0:        # its possible to append to existing subsequence
                end[x] += 1
                end[x-1] -= 1
            elif count[x+1] and count[x+2]:     # create a new subsequence
                count[x+1] -= 1
                count[x+2] -= 1
                end[x+2] += 1
            else:
                return False
        
        return True