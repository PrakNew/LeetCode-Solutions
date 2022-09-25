/*
    Time complexity : O(NlogN)
    Space complexity: O(1)
*/
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        int n = intervals.size();
        sort(intervals.begin(), intervals.end());
        int x = intervals[0][0], y = intervals[0][1];
        int ct = n;
        bool isContained;
        
        for(int i = 1; i < n; ++i){
            isContained = false;
            if(x <= intervals[i][0] && intervals[i][1] <= y) {
                ct -= 1;
                isContained = true;
            }
            else if(intervals[i][0] <= x && y <= intervals[i][1])
                ct -= 1;
            
            if(!isContained){
                x = intervals[i][0];
                y = intervals[i][1];
            }
        }
        
        return ct;
    }
};