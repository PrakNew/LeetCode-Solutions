/*
Idea: DP

Time complexity : O(m^2 * n^2)
Space complexity: O(m * n)
*/
#include<vector>
using namespace std;

class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> S(m + 1, vector<int>(n + 1, 0));
        
        for(int i = 1; i <= m; ++i)
            for(int j = 1; j <= n; ++j)
                S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + matrix[i-1][j-1];
           
        int res = 0;
        int curr = 0;
        for(int p = 1; p <= m; ++p){
            for(int r = p; r <= m; ++r){
                for(int q = 1; q <= n; ++q){
                    for(int s = q; s <= n; ++s){
                        curr = S[r][s] - S[r][q-1] - S[p-1][s] + S[p-1][q-1];
                        if(curr == target)
                            res++;
                    }
                }
            }
        }
        
        return res;
    }
};