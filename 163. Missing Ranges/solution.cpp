/*
Time complexity : O(n)
Space complexity: O(n)
*/

#include<string>
#include<vector>
using namespace std;

class Solution {
public:
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        if(nums.empty()){
            if(lower == upper)
                return {to_string(lower)};
            return {to_string(lower) + "->" + to_string(upper)};
        }
 
        int n = nums.size();
        int end = upper;
        vector<string> res;
        int i = 0;
        while(i < n){
            if(nums[i] == lower){
                lower = nums[i] + 1;
            }
            else{
                upper = nums[i] - 1;
                if(lower == upper)
                    res.push_back(to_string(lower));
                else{
                    string interval = to_string(lower) + "->" + to_string(upper);
                    res.push_back(interval);
                }
                lower = nums[i] + 1;    
            }
            i++;
        }
        
        if(lower == end)
            res.push_back(to_string(lower));
        else if(lower < end){
            string interval = to_string(lower) + "->" + to_string(end);
            res.push_back(interval);
        }  
        
        return res;
    }
};