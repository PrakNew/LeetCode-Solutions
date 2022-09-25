"""
Idea: Use prefix sum to check if target is already seen, and maintain another array to keep track of best so far length

Time complexity : O(n)
Space complexity: O(n)
"""

class Solution:
    def minSumOfLengths(self, A, target):
        n = len(A)
        best_till = [float('inf')] * n
        seen = {0: -1}
        prefix = A[:]
        best = ans = float('inf')
        
        for i in range(1, n):
            prefix[i] += prefix[i-1]
        
        for i, curr in enumerate(prefix):
            if curr - target in seen:
                end = seen[curr - target]
                if end > -1:        # wait for second match
                    ans = min(ans, i - end + best_till[end])
                best = min(best, i - end)
            
            best_till[i] = best
            seen[curr] = i
        
        return ans if ans < float('inf') else -1