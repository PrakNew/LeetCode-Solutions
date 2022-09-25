class Solution:
    def largestNumber(self, cost, target):
        
        cost = [0] + cost
        dp = {}
        
        def bigger(num1, num2):
            if '0' in num1:
                return num2
            elif '0' in num2:
                return num1
            elif int(num1) > int(num2):
                return num1
            else:
                return num2
        
        def knapsack(index, target):
            if target==0:
                return ''
            
            if target<0 or index==10:
                return '0'
            
            key = (index, target)
            
            if key not in dp:
            
                include = str(index) + knapsack(1, target - cost[index])
                exclude = knapsack(index+1, target)
                
                dp[key] = bigger(include, exclude)
            
            return dp[key]
        
        return knapsack(1, target)
            