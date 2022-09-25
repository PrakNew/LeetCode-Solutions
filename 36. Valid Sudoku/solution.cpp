/*
Time complexity: O(n^2)
Space complexity: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& A) {
        int x, y, r, c, k, i, j;
        for(x = 0; x < 9; ++x){
            for(y = 0; y < 9; ++y){
                if(A[x][y] != '.'){
                    r = x - x % 3;
                    c = y - y % 3;

                    // Check 3 x 3 grid
                    for(i = r; i < r + 3; ++i){
                        for(j = c; j < c + 3; ++j){
                            if(i != x and j != y and A[i][j] == A[x][y]){
                                return false;
                            }
                        }
                    }

                    // Check row and col
                    for(k = 0; k < 9; ++k){
                        if((k != x and A[k][y] == A[x][y]) || (k != y and A[x][k] == A[x][y])){
                            return false;
                        }
                    }
                }
            }
        }
        
                
        return true;
    }
};