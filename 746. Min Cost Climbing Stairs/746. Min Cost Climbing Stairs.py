class Solution:       
    def minCostClimbingStairs(self, cost):
        
        def topDown():
            dp = {}
            def func(i):
                if i>=len(cost):
                        return 0
                if i not in dp:
                    dp[i] = min(func(i+1), func(i+2)) + cost[i]
                return dp[i]

            return min(func(0), func(1))
        
        def bottomUp():
            n = len(cost)
            dp = [0 for _ in range(n+1)]
            dp[0] = cost[0]
            dp[1] = cost[1]

            for i in range(2, n):
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

            return min(dp[n-1], dp[n-2])
        
        def constantSpace():
            n = len(cost)
            two_step_away = cost[0]
            one_step_away = cost[1]
            for i in range(2, n):
                current_step = min(one_step_away, two_step_away) + cost[i]
                two_step_away = one_step_away
                one_step_away = current_step
            
            return min(one_step_away, two_step_away)
        
        # return topDown()
        # return bottomUp()
        return constantSpace()