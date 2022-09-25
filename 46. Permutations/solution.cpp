/*
Idea: Backtracking

Time complexity : O(n P k)
Space complexity: O(n!)
*/
#include<vector>
#include<string>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        util(0, nums, res);
        return res;
    }
private:
    void util(int start, vector<int>& nums, vector<vector<int>>& res){
        if(start == nums.size() - 1){
            res.push_back(nums);
            return;
        }
        
        for(int i = start; i < nums.size(); ++i){
            swap(&nums[start], &nums[i]);   // Swap start with index i
            util(start + 1, nums, res);
            swap(&nums[start], &nums[i]);   // Revert back the changes
        }
    }
    
    void swap(int *a, int *b){
        int temp = *a;
        *a = *b;
        *b = temp;
    }
};