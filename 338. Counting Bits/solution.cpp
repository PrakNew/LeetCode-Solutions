/*
Time complexity : O(n log n)
Space complexity: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res;
        int n, ct;
        for(int i=0;i<=num;++i)
        {
            ct = 0;
            n = i;
            while(n>0)
            {
                ct++;
                n &= (n-1);
            }
            res.push_back(ct);
        }
        return res;
    }
};