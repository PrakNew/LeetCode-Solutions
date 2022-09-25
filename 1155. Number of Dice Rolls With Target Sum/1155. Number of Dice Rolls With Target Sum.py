class Solution:
    def numRollsToTarget(self, d, f, target):
            
        def roll(i, path, target):
            
            if i==d:
                return 1 if path==target else 0
            
            key = (i, path)
            
            if key not in dp:
                res = 0
                for j in range(1, f+1):
                    if path + j <= target:
                        res += roll(i+1, path + j, target)
                    else:
                        break
                
                dp[key] = res
            
            return dp[key]
            
        dp = {} 
        return roll(0, 0, target) % 1000000007