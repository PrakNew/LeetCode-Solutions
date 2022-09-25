/*
Idea: Merge intervals

Time complexity : O(n log n)
Space complexity: O(1)
*/

#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        int n = points.size();
        if(n==0 || n==1)
            return n;
        
        sort(begin(points), end(points));
        
        int arrow = points[0][1];
        int ct = 1;
        
        for(int i = 1; i < n; ++i){
            if(points[i][0] <= arrow){
                arrow = min(arrow, points[i][1]);
            }
            else{
                arrow = points[i][1];
                ct ++;
            }
        }
       
        return ct;
    }
};