'''
Idea: Flatten the given board into a 1-D array. Perform BFS starting from first cell. In each iteration you can land in one among six possible states. Find the number of steps to reach last index in the array.

Time complexity : O(n^2)
Space complexity: O(n^2)
'''

import collections

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        A = [-1]
        rev = 0
        for i in range(n-1, -1, -1):
            row = []
            for j in range(n):
                row += board[i][j],
            if rev:
                row = row[::-1]
            rev = 1 - rev
            A += row
        
        # Start from first cell, do BFS
        q = collections.deque([(1, 0)])
        visited = set([0])
        while q:
            x, steps = q.popleft()
            if x == n*n:  # reached last cell
                return steps
            for i in (x+1, x+2, x+3, x+4, x+5, x+6):
                if i <= n*n and i not in visited:
                    visited.add(i)
                    if A[i]!=-1:
                        q.append((A[i], steps+1))
                    else:
                        q.append((i, steps+1))
        
        return -1