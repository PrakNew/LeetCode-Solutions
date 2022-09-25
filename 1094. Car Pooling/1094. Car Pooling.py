'''
Idea: Sort the trips by starting time. Maintain a min heap with trip end time as key and 
      keep popping trips out as and when current start time is greater than or equal to
      top of heap.

Time complexity : O(n)
Space complexity: O(n)
'''

import heapq

class Solution:
    def carPooling(self, trips, capacity):
        n = len(trips)
        if n==0:
            return True
        # Sort trip by start time
        trips.sort(key = lambda trip: trip[1])
        cars = []
        heapq.heappush(cars, (trips[0][2], trips[0][0]))
        size = trips[0][0]
        for i in range(1, n):
            while cars and cars[0][0] <= trips[i][1]:
                size -= cars[0][1]
                heapq.heappop(cars)
            heapq.heappush(cars, (trips[i][2], trips[i][0]))
            size += trips[i][0]
            if size > capacity:
                return False
        
        return True
        

        