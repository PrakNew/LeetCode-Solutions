/*
    Time complexity : O(log N)
    Space complexity: O(1)
*/

#include<iostream>
#include<cmath>
using namespace std;

class Solution {
public:
    int findComplement(int N) {
        if(N==0)
            return 1;
        int ct = 0, num = N, mask;
        while(num){
            ct++;
            num >>= 1;
        }
        mask = pow(2, ct) - 1;
        return N ^ mask;
    }
};