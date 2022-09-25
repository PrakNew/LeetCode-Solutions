/*
Time complexity : O(n)
Space complexity: O(1)
*/
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int m = arrays.size();
        int n = arrays[0].size();
        int max_val = arrays[0][0], min_val = arrays[0][arrays[0].size()-1];
        int res = 0;
        for(int i = 0; i < m; ++i){
            res = max(res, max(abs(max_val - arrays[i][0]), abs(arrays[i][arrays[i].size()-1] - min_val)));
            max_val = max(max_val, arrays[i][arrays[i].size() - 1]);
            min_val = min(min_val, arrays[i][0]);
        }
        return res;
    }
};