/*
Idea: Kadane's algorithm

    Time complexity: O(n)
    Space complexity: O(1)
*/

#include<vector>
#include<climits>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int max_so_far = INT_MIN, curr = 0;
        for(auto x: nums){
            curr += x;
            max_so_far = max(max_so_far, curr);
            curr = max(0, curr);
        }
        return max_so_far;
    }
};