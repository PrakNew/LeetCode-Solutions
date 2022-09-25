class Solution:
    def merge(self, intervals):
        n = len(intervals)
        intervals.sort()
        merged = []
        
        for i in range(n):
            if merged == [] or merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
        
        return merged