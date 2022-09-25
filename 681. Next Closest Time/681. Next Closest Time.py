"""
Idea: From set of all possible two digits in ascending order, find next closest minute/hour

Time complexity : O(1)  max possible combinations is 4^4
Space complexity: O(1)
"""

class Solution:
    def nextClosestTime(self, time):
        hour, minute = time.split(':')
        
        sorted_digits = sorted(set(hour + minute))
        possible_digits = [a + b for a in sorted_digits for b in sorted_digits]
        
        # check next possible minute lies within the hour
        index = possible_digits.index(minute)
        if index + 1 < len(possible_digits) and possible_digits[index + 1] < "60":  # valid minute
            return hour + ":" + possible_digits[index + 1]
        
        # check if hour lies within the day
        index = possible_digits.index(hour)
        if index + 1 < len(possible_digits) and possible_digits[index + 1] < "24":  # valid hour
            return possible_digits[index + 1] + ":" + sorted_digits[0] + sorted_digits[0]
        
        # earliest time next day
        return sorted_digits[0] + sorted_digits[0] + ":" + sorted_digits[0] + sorted_digits[0]
        