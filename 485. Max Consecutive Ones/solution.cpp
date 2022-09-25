/*
Time complexity : O(n)
Space complexity: O(1)
*/

#include<vector>

using namespace std;

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& A) {
        if(A.empty())
            return 0;
        
        int res = 0, ct = 0, prev = -1;
        
        for(auto x: A){
            if(prev and x==1)
                ct++;
            else if(x==1)   
                ct = 1;
            
            prev = x;
            res = max(res, ct);
        }
        
        return res;
    }
};