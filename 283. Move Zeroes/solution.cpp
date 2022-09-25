/*
    Time complexity : O(n)
    Space complexity: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int k = 0, temp;
        for(int i = 0; i < n; ++i){
            if(nums[i] != 0){
                temp = nums[i];
                nums[i] = nums[k];
                nums[k] = temp;
                k++;
            }
        }
    }
};