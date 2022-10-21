/*
Time complexity : O(n)
Space complexity : O(min(n, k))
*/
// easy solution just brute force
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int,int> ma;
        for (int i=0;i<nums.size();i++){
            if (ma.find(nums[i])!=ma.end()){
                int d=i-ma[nums[i]];
                if (d<=k){
                    return true;
                }
                ma[nums[i]]=i;
            }
            else{
                ma[nums[i]]=i;
            }
        }
        return false;
    }
};

#include<vector>
#include<map>
using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        int n = nums.size();
        map<int, int> seen;
        for(int i = 0; i < n; ++i){
            if(seen[nums[i]] != 0 and abs(seen[nums[i]] - i - 1) <= k){
                return true;
            }
            
            seen[nums[i]] = i + 1;

            if(seen.size() > k){
                seen.erase(nums[i-k]);
            }
        }
        return false;
    }
};