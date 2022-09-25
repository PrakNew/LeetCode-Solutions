'''
Idea : Sort intervals by ending time. Check if current interval does not overlap with previous interval

Time complexity : O(n)
Space complexity: O(1)
'''

class Solution:
    def eraseOverlapIntervals(self, intervals):
        n = len(intervals)        
        if n==0:
            return 0
        # sort intervals by ending time
        intervals.sort(key = lambda interval: interval[1])
        remove = 0
        res = [intervals[0]]
        prev_ending = intervals[0][1]
        for i in range(1, n):
            if prev_ending <= intervals[i][0]:
                res += intervals[i],
                prev_ending = intervals[i][1]
            else:
                remove += 1
        return remove