"""
Idea: Backtracking using branch cutting

O(k!) -> until all zeros are filled
O(k^(n-k)) -> after every element in subset is non-zero

Time complexity : O(k^(n-k) * k!)       
Space complexity: O(n)

"""

class Solution:
    def canPartitionKSubsets(self, nums, k):
        
        if sum(nums)%k!=0 or len(nums) < k:
            return False
        
        n = len(nums)
        workers = [0] * n
        nums.sort(reverse = True)
        self.res = sum(nums)//k
        
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