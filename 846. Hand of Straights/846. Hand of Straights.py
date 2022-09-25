"""
Idea: Greedily check if its possible to arrange the cards starting from minimum

Time complexity : O(n log n)
Space complexity: O(n)
"""
import collections

class Solution:
    def isNStraightHand(self, hand, W):
        count = collections.Counter(hand)
        while count:
            start = min(count)
            for w in range(start, start + W):
                if w not in count:
                    return False
                count[w] -= 1
                if count[w] == 0:
                    del count[w]
        
        return True
    