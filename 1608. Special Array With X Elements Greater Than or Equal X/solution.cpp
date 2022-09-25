#include<iostream>
#include<vector>
using namespace std;


class Solution {
public:
    int specialArray(vector<int>& nums) {
        int n = nums.size();
        int lo = 0, hi = n;
        while(lo <= hi){
            int mid = (lo+hi)>>1;
            int ct = count(nums, mid);
            if( ct == mid)
                return mid;
            else if(ct < mid)
                hi = mid - 1;
            else
                lo = mid + 1;
        }
        return -1;
    }
    
    private: 
    int count(vector<int> &A, int k) {
        int ct = 0;
        for(auto x: A)
            if(x >= k)
                ct++;
        return ct;
    }
};