#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& A, int target) {
        int m = A.size();
        if(m==0)
            return false;
        int n = A[0].size();
        int lo = 0, hi = m * n - 1, x, y;
        while(lo <= hi){
            int mid = (lo + hi) >> 1;
            x = mid/ n ;
            y = mid % n;
            if(A[x][y] == target)
                return true;
            else if(A[x][y] < target){
                lo = mid + 1;
            }
            else{
                hi = mid - 1;
            }
        }
        return false;
    }
};