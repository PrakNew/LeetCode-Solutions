/*
    Time complexity : O(n)
    Space complexity: O(1)
*/

#include<iostream>
using namespace std;

class Solution {
public:
    int countPrimeSetBits(int L, int R) {
        // vector<int> primes {2, 3, 5, 7, 11, 13, 17, 19};
        // int BINARY = 0;
        // for(auto k : primes){
        //     BINARY += pow(2, k);
        // }
        int BINARY = 665772;
        int ct = 0;
        for(int i = L; i <= R; ++i)
            if(BINARY >> __builtin_popcount(i) & 1)     // if i'th bit is set, then it is prime number
                ct++;
        return ct;
    }    
};