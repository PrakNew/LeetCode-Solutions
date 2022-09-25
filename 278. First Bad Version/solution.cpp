/*
Time complexity : O(log n)
Space complexity: O(1)
*/

#include<queue>
using namespace std;

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int lo = 1, hi = n;
        while(lo < hi){
            int mid = lo + ((hi - lo) >> 1);
            if(isBadVersion(mid)){
                hi = mid;
            }
            else
                lo = mid + 1;
        }
        return lo;
    }
};