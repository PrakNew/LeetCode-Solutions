/*
Idea: Total XOR of all the numbers will give XOR of two missing numbers. To differentiate
      these two numbers, we create a mask (first set bit in the total). Rightmost set bit 
      which is basically mask will be different for both the missing numbers. 

Time complexity : O(n)
Space complexity: O(1)
*/


#include<vector>
using namespace std;

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int missings = 0;
        for(auto x: nums)
            missings ^= x;
        
        // returns first set bit
        int mask = -missings & missings;  
        int first = 0, second = 0;
        for(auto x: nums){
            if(x & mask)
                first ^= x;
            else
                second ^= x;
        }
        
        return {first, second};
    }
};