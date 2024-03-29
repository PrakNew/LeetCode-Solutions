# Here I am inserting the newInterval element to the bisect_left value and simply following the pattern of insertion 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insertI = bisect_left(intervals, newInterval)
        intervals.insert(insertI, newInterval)
        stack = []
        print(intervals)
        for s,e in intervals:
            if stack and stack[-1][1] >= s: #pattern of insertion 
                lastS,lastE = stack.pop()
                stack.append([lastS, max(lastE,e)])
            else:
                stack.append([s,e])
        return stack





'''
Idea: First insert intervals towards left of the newInterval. Then merge all the intervals which intersect with new
      interval. Add the new interval to the result, followed by all the intervals to the right of the new interval
     
Time complexity : O(n)
Space complexity: O(1) excluding result array
'''

class Solution:
    def insert(self, intervals, newInterval):
        n = len(intervals)
        merged = []
        
        i = 0
        
        # Insert intervals to the left of the new interval
        while i < n and intervals[i][1] < newInterval[0]:
            merged += intervals[i],
            i += 1
        
        # Merge intervals that intersect with new Interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        merged += newInterval,
        
        # Insert intervals to the right of the new interval
        while i < n:
            merged += intervals[i],
            i += 1
                    
        return merged
        
        