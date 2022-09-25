/*
    Time complexity : O(log N)
    Space complexity: O(1)
*/

#include<iostream>
using namespace std;


class Solution {
public:
    bool hasAlternatingBits(int n) {
        int num = n;
        int prev = -1;
        while(num){
            if(prev!=-1){
                if((1 - prev) != num%2)
                    return false;
            }
            prev = num%2;
            num >>= 1;
        }
        return true;
    }
};