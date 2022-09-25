/*
Idea: DP

    Time complexity: O(n)
    Space complexity: O(n)
*/

#include<vector>
#include<climits>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> dp(nums.size(), -1);
        return util(nums, 0, dp);
    }
    
private:
    
    int util(vector<int>& nums, int i, vector<int>& dp){
        if(i >= nums.size())
            return 0;
        
        if(dp[i] != -1)
            return dp[i];
        
        int include = nums[i] + util(nums, i + 2, dp);
        int exclude = util(nums, i + 1, dp);
        
        dp[i] = max(include, exclude);
        
        return dp[i];
    }
};