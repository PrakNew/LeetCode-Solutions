/*
Idea: DP

Time complexity : O(m * n)
Space complexity: O(n)
*/
#include<vector>
#include<map>
#include<queue>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {        
        vector<int> first(n, 1);
        vector<int> second(n, 0);
        
        for(int i = 1; i < m; ++i){
            second[0] = 1;
            for(int j = 1; j < n; ++j)
                second[j] = first[j] + second[j-1];
            first = second;
        }
        
        return first[n-1];
    }
};