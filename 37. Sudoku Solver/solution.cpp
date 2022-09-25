/*
Idea: Backtracking. Find empty cells and try all possible digits in that cell. If a path conflicts, backtrack and try
      a different digit.
*/
#include<iostream>
#include<vector>

using namespace std; 

class Solution {
    private:
        vector<int> findEmptyCell(vector<vector<char> > &A){
            vector<int> res(2, -1);
            for(int i = 0; i < 9; ++i){
                for(int j = 0; j < 9; ++j){
                    if(A[i][j] == '.') {
                        res[0] = i;
                        res[1] = j;
                        return res;
                    }
                }
            }
            return res;
        }
        
        bool canFill(vector<vector<char> > &A, int x, int y, char digit){
            int row = (x/3)*3;
            int col = (y/3)*3;
            
            // Check 3 x 3 grid
            for(int i = 0; i < 3; ++i)
                for(int j = 0; j < 3; ++j){
                    if(A[row+i][col+j] == digit)   
                        return false;
                }
            
            // Check row and column
            for(int i = 0; i < 9; ++i)
                if(A[x][i] == digit || A[i][y] == digit)
                    return false;
            
            return true;
        }
    
        bool solveUtil(vector<vector<char> > &A){
            vector<int> empty =  findEmptyCell(A);
            
            if(empty[0]==-1)    // Board is filled
                return true;
            
            
            int x = empty[0], y = empty[1];
            
            // Try digits one by one
            for(int i = 1; i < 10; ++i){
                char digit = '0' + i;
                if(canFill(A, x, y, digit)){
                    A[x][y] = digit;
                    if(solveUtil(A))   // if solved return
                       return true;
                    A[x][y] = '.';      // Otherwise backtrack
                }
            }
            
            // Prune
            return false;
        }
    
    
    
    public:
        void solveSudoku(vector<vector<char>>& board) {
            int m = board.size();
            int n = board[0].size();

            if(solveUtil(board))
                ;// do nothing
        }
};