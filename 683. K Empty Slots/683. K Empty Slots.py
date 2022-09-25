"""
Idea: Sliding window 

Time complexity : O(n)
Space complexity: O(n)
"""

class Solution:
    def kEmptySlots(self, bulbs, k):
        n = len(bulbs)
        days = [0] * n
        for day, bulb in enumerate(bulbs, 1):
            days[bulb-1] = day
        
        left, right = 0, k + 1
        res = float('inf')
        
        while right < n:
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:       # some bulb between left and right is switched on
                    left, right = i, i + k + 1
                    break
            else:       # no in between bulbs is switched on
                curr_ans = max(days[left], days[right])
                res = min(res, curr_ans)
                left, right = right, right + k + 1
        
        return res if res < float('inf') else -1