"""
Idea: Dynamic Programming - For each pair of possible sum, update the dictionary with largest possible
      value .

Time complexity: O(n*sum)
Space complexity: O(n*sum)
"""
import collections

class Solution:
    def tallestBillboard(self, rods):
        n = len(rods)
        dp = collections.defaultdict(int)
        dp[0] = 0
        
        for rod in rods:
            mp = collections.defaultdict(int)
            for s in dp:
                mp[s + rod] = max(dp[s] + rod, mp[s + rod])
                mp[s - rod] = max(dp[s], mp[s - rod])
                mp[s] = max(dp[s], mp[s])
            dp = mp
        
        return dp[0]
        
                
            
        