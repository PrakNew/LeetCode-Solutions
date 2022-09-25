/*
Idea: Backtracking

Time complexity : O(2^n)
Space complexity: O(2^n)
*/
#include<vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> curr;
        for(int len = 0; len <= nums.size(); ++len)
            util(0, len, curr, nums, res);
        return res;
    }
private:
    void util(int start, int end, vector<int>& curr, vector<int>& nums, vector<vector<int>>& res){
        if(curr.size() == end){
            res.push_back(curr);
        }
        for(int i = start; i < nums.size(); ++i){
            curr.push_back(nums[i]);
            util(i + 1, end, curr, nums, res);
            curr.pop_back();
        }
    }
};