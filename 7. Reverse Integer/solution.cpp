/*
Time complexity: O(log n)
Space complexity: O(1)
*/

#include<climits>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        int res = 0, temp = x;
        while(temp){
            int dgt = temp % 10;
            if(res > INT_MAX / 10 || (res == INT_MAX / 10 and dgt > 7))
                return 0;
            if(res < INT_MIN / 10 || (res == INT_MIN / 10 and dgt < -8))
               return 0;
            res *= 10;
            res += dgt;
            temp /= 10;
        }
        return res;
    }
};