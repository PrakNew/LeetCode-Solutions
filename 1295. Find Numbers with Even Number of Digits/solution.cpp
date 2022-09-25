/*
Time complexity : O(d * n) where d is the maximum number of digits in a number
Space complexity: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    int findNumbers(vector<int>& A) {
        int n = A.size();
        int res = 0;
        for(auto x : A)
            if(getDigits(x))
                res++;
        return res;
    }
private:
    int getDigits(int n){
        int ct = 0;
        while(n){
            ct ^= 1;
            n /= 10;
        }
        return ct == 0;
    }
};