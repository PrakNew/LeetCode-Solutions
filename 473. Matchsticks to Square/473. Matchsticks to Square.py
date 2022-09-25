"""
Idea: Backtracking using branch cutting technique.

Time complexity : O(n^(n-4) * 4!)
Space complexity: O(n)
"""

class Solution:
    def makesquare(self, nums):
        if sum(nums) % 4 != 0 or len(nums) < 4:
            return False
        
        k = 4
        n = len(nums)
        workers = [0] * k
        nums.sort(reverse = True)
        self.res = sum(nums)//4
        
        def dfs(curr):
            if curr == n:
                return True
            
            seen = set()
            for i in range(k):
                if (workers[i] in seen) or (workers[i] + nums[curr] > self.res):
                    continue 
                seen.add(workers[i])
                workers[i] += nums[curr]
                if dfs(curr+1):
                    return True
                workers[i] -= nums[curr]
        
            return False
        
        return dfs(0)
        
                    
        