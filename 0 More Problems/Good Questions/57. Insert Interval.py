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