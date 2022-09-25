"""
Idea: Backtracking with branch cutting technique
"""

class Solution:
    def minimumTimeRequired(self, jobs, k):
        workers = [0] * k
        self.res = float('inf')
        
        def dfs(curr):
            if curr == len(jobs):
                self.res = min(self.res, max(workers))
                return 
            
            seen = set()
            for i in range(k):
                if (workers[i] in seen) or (workers[i] + jobs[curr] >= self.res):
                    continue
                seen.add(workers[i])
                workers[i] += jobs[curr]
                dfs(curr+1)
                workers[i] -= jobs[curr]
            
        dfs(0)
        return self.res
        