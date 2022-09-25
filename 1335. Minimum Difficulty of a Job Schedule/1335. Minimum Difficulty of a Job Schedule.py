"""
Idea: DP

Time complexity: O(n * d * n)
Space complexity: O(n * d)
"""

import functools

class Solution:
    def minDifficulty(self, jobs, d):
        n = len(jobs)
        
        if n < d:
            return -1
        
        @functools.lru_cache(None)
        def maxJob(i, d):
            if d == 1:
                return max(jobs[i:])
            
            res = float('inf')
            max_job = jobs[i]
            
            for j in range(i, n - d + 1):
                max_job = max(max_job, jobs[j])
                res = min(res, max_job + maxJob(j + 1, d - 1))
            
            return res
        
        return maxJob(0, d)