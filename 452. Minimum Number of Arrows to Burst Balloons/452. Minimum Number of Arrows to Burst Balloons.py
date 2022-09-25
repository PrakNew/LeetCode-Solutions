'''
Idea : Sort the intervals based on starting time. Use two pointers to keep track of overlapping intervals.

Time complexity : O(n)
Space complexity: O(1)

'''

class Solution:
    def findMinArrowShots(self, A):
        n = len(A)
        A.sort()
        
        arrows = 0
        i = 0
        
        while i < n:
            start = A[i][0]
            end = A[i][1]
            j = i + 1
            while j < n and A[j][0] <= end:
                start = max(start, A[j][0])   
                end = min(end, A[j][1])
                j += 1
            arrows += 1
            i = j
        
        return arrows