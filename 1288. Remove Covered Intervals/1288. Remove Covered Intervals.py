"""
    Time complexity : O(NlogN)
    Space complexity: O(1)
"""

class Solution:
    def removeCoveredIntervals(self, intervals):
        n = len(intervals)
        intervals.sort()
        ct = n
        x, y = intervals[0][0], intervals[0][1]

        for i in range(1, n):
            if x <= intervals[i][0] and intervals[i][1] <= y: 
                ct -= 1
            elif intervals[i][0] <= x and y <= intervals[i][1]:
                ct -= 1
                x = intervals[i][0]
                y = intervals[i][1]
            else:
                x = intervals[i][0]
                y = intervals[i][1]
        
        return ct