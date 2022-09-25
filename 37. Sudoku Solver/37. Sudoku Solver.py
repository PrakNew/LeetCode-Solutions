"""
Idea: Backtracking. Find empty cells and try all possible digits in that cell. If a path conflicts, backtrack and try
      a different digit.
"""

class Solution:
    
    def findCell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j]=='.':
                    return i, j
        return -1, -1
    
    def isSafe(self, x, y, dgt):
        row = x - x%3
        col = y - y%3
        
        for i in range(3):
            for j in range(3):
                if self.board[row+i][col+j]==str(dgt):
                    return False 
        
        for i in range(9):
            if self.board[x][i]==str(dgt) or self.board[i][y]==str(dgt):
                return False 
        
        return True
    
    
    def util(self):
        row, col = self.findCell()
        
        if row==-1:
            return True
        
        for dgt in range(1, 10):
            if self.isSafe(row, col, dgt):
                self.board[row][col] = str(dgt)
                if self.util():
                    return True
                self.board[row][col] = "." # backtrack
        
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.util() 
        