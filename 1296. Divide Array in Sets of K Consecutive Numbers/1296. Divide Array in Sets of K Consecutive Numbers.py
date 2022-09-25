"""
Idea: Greedily check if its possible to arrange the cards starting from minimum

Time complexity : O(n log n)
Space complexity: O(n)
"""
import collections

class Solution:
    def isPossibleDivide(self, A, k):
        count = collections.Counter(A)
        
        while count:
            start = min(count)
            for x in range(start, start + k):
                if x not in count:
                    return False 
                count[x] -= 1
                if count[x] == 0:
                    del count[x]
        
        return True