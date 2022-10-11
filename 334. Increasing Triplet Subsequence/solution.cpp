/*
Time complexity : O(n)
Space complexity: O(1)
*/

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if(nums.size()<3)
            return false;
        int minm=nums[0],maxm=INT_MAX;
        for(int i=1;i<nums.size();i++){
            if(nums[i]==minm)
                continue;
            if(nums[i]<minm)
                minm=nums[i];
            else if(nums[i]<maxm)
                maxm=nums[i];
            else if(nums[i]>maxm)
                return true;
        }
        return false;
    }
};

/*
Time complexity : O(n)
Space complexity: O(n)
*/

#include<vector>
#include<climits>
using namespace std;

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int first = INT_MAX, second = INT_MAX;
        for(auto x : nums){
            if(x <= first)
                first = x;
            else if(x <= second)
                second = x;
            else
                return true;
        }
        return false;
    }
};