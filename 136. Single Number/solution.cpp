/*
Idea: Properties of XOR, ie., a ^ a = 0

Time complexity : O(n)
Space complexity: O(1)
*/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int missing = 0;
        for(auto x: nums)
            missing ^= x;
        return missing;
    }
};