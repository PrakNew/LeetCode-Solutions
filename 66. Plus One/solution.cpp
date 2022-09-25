/*
Time complexity : O(n)
Space complexity: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1, sum;
        int n = digits.size();
        for(int i = n - 1; i >=0; --i){
            sum = digits[i] + carry;
            carry = sum / 10;
            digits[i] = sum % 10;
        }
        
        if(carry){
            digits[0] = 1;
            digits.push_back(0);
        }
        
        return digits;
    }
};