"""
Time complexity : O(n^2)
Space complexity: O(1)
"""

class Solution:
    def isValidSudoku(self, board):
        
        n, m = len(board), len(board[0])
        
        def isSafe(x, y, board):
            row = x - x%3
            col = y - y%3
            dgt = board[x][y]
            
            for i in range(3):
                for j in range(3):
                    if (row+i)!=x and (col+j)!=y and board[row+i][col+j]==dgt:
                        return False
            
            for i in range(9):
                if (i!=x and board[i][y]==dgt) or (i!=y and board[x][i]==dgt):
                    return False
            
            return True
        
        
        for i in range(n):
            for j in range(m):
                if board[i][j]!='.' and not isSafe(i, j, board):
                    return False
        
        return True