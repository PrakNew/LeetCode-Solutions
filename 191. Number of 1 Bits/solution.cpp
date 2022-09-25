/*
    Time complexity : O(log N)
    Space complexity: O(1)
*/

#include<iostream>
using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ct = 0;
        while(n){
            ct++;
            n &= (n-1);     // skips to next set bit from left
        }
        return ct;
    }
};