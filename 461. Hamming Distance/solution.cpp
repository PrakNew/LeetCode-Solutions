/*
Time complexity : O(log n)
Space complexity: O(1)
*/

#include<cmath>
using namespace std;

class Solution {
public:
    int hammingDistance(int x, int y) {
        int ct = 0;
        while(x and y){
            ct += (x % 2) != (y % 2);
            x >>= 1;
            y >>= 1;
        }
        
        while(x){
            ct += (x&1);
            x >>= 1;
        }
        
        while(y){
            ct += (y&1);
            y >>= 1;
        }
        
        return ct;
    }
};