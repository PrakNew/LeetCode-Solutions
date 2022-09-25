'''
Idea: Partition both the arrays into two halves such that all the elements on the left half are smaller than
      all the elements on the right half

Time complexity : O(log(min(m, n)))
Space complexity: O(1)
'''


class Solution:
    def findMedianSortedArrays(self, A, B):
        
        def median(X, Y, m, n):
            if m > n:
                return median(Y, X, n, m)
            l, r = 0, m
            size = (m+n)
            while l<=r:
                x = (l+r)>>1
                y = ((size+1)>>1) - x          # Formula: x + y = (Total Size)/2
                minRightX = minRightY = float('inf')
                maxLeftX = maxLeftY = float('-inf')
                if x > 0:   maxLeftX = X[x-1]
                if y > 0:   maxLeftY = Y[y-1]
                if x < m:   minRightX = X[x]
                if y < n:   minRightY = Y[y]
                if maxLeftX <= minRightY and maxLeftY <= minRightX:
                    if (m+n)&1:
                        return max(maxLeftX, maxLeftY)
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) * 0.5
                elif maxLeftX > minRightY:
                    r = x - 1
                else:
                    l = x + 1
                
        
        return median(A, B, len(A), len(B))