"""
Idea: Hashmap 

Time complexity : O(n)
Space complexity: O(n)
"""
import collections

class Solution:
    def minDominoRotations(self, A, B):
        n = len(A)
        
        # find the common value
        mp = collections.defaultdict(int)
        for i in range(n):
            mp[A[i]] += 1
            mp[B[i]] += 1
        
        val = max(mp, key = lambda item: mp[item])
        
        first_row = 0
        second_row = 0
        
        for i in range(n):
            if val in [A[i], B[i]]:
                if A[i] != B[i]:
                    if A[i] == val:
                        first_row += 1
                    else:
                        second_row += 1
            else:
                return -1
            
        return min(first_row, second_row)
        