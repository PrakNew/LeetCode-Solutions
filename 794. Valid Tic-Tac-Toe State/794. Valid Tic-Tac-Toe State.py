class Solution:
    def validTicTacToe(self, A):
        
        def gameOver(player):
            if player: # X won
                for i in range(3):
                    if A[i][0]==A[i][1]==A[i][2]=='X':
                        return True
                for j in range(3):
                    if A[0][j]==A[1][j]==A[2][j]=='X':
                        return True
                if A[0][0]==A[1][1]==A[2][2]=='X' or A[0][2]==A[1][1]==A[2][0]=='X':
                    return True
                return False
            else:
                for i in range(3):
                    if A[i][0]==A[i][1]==A[i][2]=='O':
                        return True
                for j in range(3):
                    if A[0][j]==A[1][j]==A[2][j]=='O':
                        return True
                if A[0][0]==A[1][1]==A[2][2]=='O' or A[0][2]==A[1][1]==A[2][0]=='O':
                    return True
                return False
            
            
        x_count = 0
        o_count = 0
        
        for i in range(3):
            for j in range(3):
                if A[i][j]=='X':
                    x_count += 1
                elif A[i][j]=='O':
                    o_count += 1
        
        if x_count < o_count or abs(x_count - o_count) > 1:
            return False
        
        if gameOver(1): # X has won
            if x_count!=o_count+1 or gameOver(0): # O cannot win
                return False
            
        
        if gameOver(0): # O has won
            if x_count!=o_count or gameOver(1): # X cannot win
                return False
        
        return True
            
                
        