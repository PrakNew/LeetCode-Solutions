'''
Idea: Start from first station. Keep track of total gas and current gas. Whenever current gas falls below 0, make the next station as new starting point. At the end, if total gas is non-negative return starting point.

Time complexity : O(n)
Space complexity: O(1)
'''

class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        total_gas = current_gas = 0
        starting_point = 0
        for i in range(n):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                starting_point = i+1
                current_gas = 0
        
        return starting_point if total_gas >= 0 else -1
        
        