/*
Time complexity: O(n^2)
Space complexity: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& A) {
        int n = A.size();
        
        // Swap elements along left diagonal
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < i; ++j){
                swap(&A[i][j], &A[j][i]);
            }
        
        // Reverse each row
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < (n>>1); ++j)
                swap(&A[i][j], &A[i][n-j-1]);
        
    }
private:
    void swap(int* a, int* b){
        int temp = *a; 
        *a = *b;
        *b = temp;
    }
};