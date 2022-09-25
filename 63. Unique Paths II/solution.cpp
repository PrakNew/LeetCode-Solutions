/*
Idea: DP

Time complexity : O(m * n)
Space complexity: O(n)
*/
#include<vector>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& A) {
        int m = A.size(), n = A[0].size();
        if(A[0][0] == 1)
            return 0;
        
        vector<int> first(n, 0);
        vector<int> second(n, 0);
        
        first[0] = A[0][0] != 1;
                
        // first row
        for(int j = 1; j < n; ++j)
            if(A[0][j] != 1)
                first[j] = first[j-1];
        
        if(m==1)
            return first[n-1];
        
        bool first_col = 1;
        for(int i = 1; i < m; ++i){
            if(A[i][0] == 1)
                first_col = 0;
            second[0] = first_col;
            for(int j = 1; j < n; ++j){
                if(A[i][j] == 1){
                    second[j] = 0;
                    continue;
                }
                second[j] = second[j-1] + first[j];
            }
            first = second;
        }
        
        return second[n-1];
    }
};