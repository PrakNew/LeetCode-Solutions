#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n==1)
            return nums[0];
        vector<int> dp1(n, -1);
        vector<int> dp2(n, -1);
        int one = util(nums, 0, n-1, dp1);
        int two = util(nums, 1, n, dp2);
        return max(one, two);
    }
private:
    int util(vector<int> &A, int index, int last, vector<int>& dp){
        if(index >= last)
            return 0;
        
        if(dp[index] != -1)
            return dp[index];
        
        int include = A[index] + util(A, index + 2, last, dp);
        int exclude = util(A, index + 1, last, dp);
        
        dp[index] = max(include, exclude);
        
        return dp[index];
    }
};