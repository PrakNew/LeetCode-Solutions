/*
Time complexity : O(1)
Space complexity: O(1)
*/

#include<cmath>
using namespace std;


class Solution {
public:
    bool isPowerOfThree(int n) {
        return n > 0 and (int) pow(3, 19) % n == 0;
    }
};