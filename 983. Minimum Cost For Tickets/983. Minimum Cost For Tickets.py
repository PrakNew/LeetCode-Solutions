class Solution:
    def mincostTickets(self, days, costs):
        
        daySet = set(days)
        dp = {}
        firstDay, lastDay = days[0], days[-1]
        
        def fn(day):
            if day > lastDay:
                return 0
            
            if day in dp:
                return dp[day]
            
            if day in daySet: # choose one among three
                dp[day] = min(fn(day+1) + costs[0], fn(day+7) + costs[1], fn(day+30) + costs[2])
            else: # wait for travel day
                dp[day] = fn(day+1)
                
            return dp[day]
        
        return fn(firstDay)
    
                