#include<vector>
#include<map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> mp;
        int n = nums.size(), complement;
        
        for(int i = 0; i < n; ++i){
            complement = target - nums[i];
            if(mp.find(complement) != mp.end())
                return {i, mp[complement]};
            
            mp[nums[i]] = i;
        }
            
        return {-1, -1};
    }
};