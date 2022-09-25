/*
Time complexity : O(n)
Space complexity: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();

        vector<int> res(begin(nums), end(nums));
        
        // Store left product in array itself
        for(int i = 1; i < n; ++i){
            res[i] *= res[i-1];
        }
        
        int R = 1; // Keeps track of right product
        for(int i = n-1; i >= 1; --i){
            res[i] = res[i-1] * R;
            R *= nums[i];
        }
        
        res[0] = R;
        
        return res;
    }
};