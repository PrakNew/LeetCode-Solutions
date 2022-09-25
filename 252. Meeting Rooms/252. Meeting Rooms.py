'''
Idea: Sort the meetings by their starting time

Time complexity : O(n)
Space complexity: O(1)

'''

class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort()
        n = len(intervals)
        for i in range(1, n):        
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True