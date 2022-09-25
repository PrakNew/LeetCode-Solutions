'''
Time complexity : O(N log N)
Space complexity: O(N)
'''

import collections, bisect

class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        if n==1:
            return [-1]
        
        # Store the original indices of interval 
        index_interval = collections.defaultdict()
        for index, interval in enumerate(intervals):
            index_interval[tuple(interval)] = index
            
        # Sort the intevals based on their start time
        sorted_intervals = intervals[::]
        sorted_intervals.sort()
        start_times = [interval[0] for interval in sorted_intervals]
        res = []
        for i in range(n):
            # find the next interval with earliest start time
            lindex = bisect.bisect_left(start_times, intervals[i][1])
            if lindex < n:
                res.append(index_interval[tuple(sorted_intervals[lindex])])
            else:
                res.append(-1)
     
        return res