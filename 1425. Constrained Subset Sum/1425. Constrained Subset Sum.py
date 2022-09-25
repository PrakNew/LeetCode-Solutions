"""
Idea: Use deque

Time complexity: O(n)
Space complexity: O(k)

"""

import collections

class Solution:
    def constrainedSubsetSum(self, A, k):

        n = len(A)
        q = collections.deque()
        
        for i in range(n):
            A[i] += q[0] if q else 0
            
            while q and A[i] > q[-1]:
                q.pop()
            
            if A[i] > 0:
                q.append(A[i])
            
            if i >= k and q and q[0] == A[i-k]:
                q.popleft()
        
        return max(A)