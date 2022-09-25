/*
Idea: Properties of &, ^ and ~

Time complexity : O(n)
Space complexity: O(1)s
*/

#include<vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int seenOnce = 0, seenTwice = 0;
        
        for(auto num : nums){
            seenOnce = ~seenTwice & (seenOnce ^ num);
            seenTwice = ~seenOnce & (seenTwice ^ num);
        }
        
        return seenOnce;
    }
};