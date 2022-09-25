'''
Idea: Sort meetings based on their starting time. Use min heap with meeting end time as key to check how many rooms are needed.

Time complexity : O(n log n)
Space complexity: O(n)
'''
import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        n = len(intervals)
        if n==0:
            return 0
        intervals.sort(key = lambda interval: interval[0])
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        for interval in intervals[1:]:
            if rooms[0] <= interval[0]: # meeting has concluded so room can be emptied
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])
            
        return len(rooms)
        
        
         