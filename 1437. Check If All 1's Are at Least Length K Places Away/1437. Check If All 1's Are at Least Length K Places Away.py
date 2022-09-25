"""
Time complexity : O(n)
Space complexity: O(1)
"""

class Solution:
    def kLengthApart(self, A, k):
        n = len(A)
        i = 0
        ct = 0
        while i < n:
            if A[i] == 1:
                if ct > 0:
                    return False
                ct = k + 1
            ct -= 1
            i += 1
        
        return True
        