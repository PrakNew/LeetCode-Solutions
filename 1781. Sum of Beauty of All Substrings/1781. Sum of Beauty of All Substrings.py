"""
Idea: Use multiset to get most and least frequent elements in constant time

Time complexity : O(n * n log n)
Space complexity: O(n)
"""

from sortedcontainers import SortedList
import collections

class Solution:
    def beautySum(self, s):
        n = len(s)
        res = 0
        
        for i in range(n):          # O(n)
            
            freq = collections.defaultdict(int)
            multiset = SortedList([])
            
            for j in range(i, n):       # O(n)
                f = freq[s[j]]
                freq[s[j]] += 1
                
                if f > 0:
                    multiset.remove(f)
                
                multiset.update([f+1])      # O(log n)
                
                res += multiset[-1] - multiset[0]
        
        return res