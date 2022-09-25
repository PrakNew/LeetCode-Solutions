'''
Idea: Start from top-right/bottom-left element. Do a search space reduction and keep updating
      row and col values accordingly.

Time complexity : O(m+n)
Space complexity: O(1)
'''
class Solution:
    def searchMatrix(self, A, target):
        if A==[]:
            return False
        m, n = len(A), len(A[0])
        row = 0
        col = n-1
        while row<m and col>=0:
            if A[row][col]==target:
                return True
            if A[row][col] > target:
                col -= 1
            else:
                row += 1
        
        return False