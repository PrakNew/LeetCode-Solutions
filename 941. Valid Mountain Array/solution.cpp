/*
    Time complexity : O(n)
    Space complexity: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    bool validMountainArray(vector<int>& A) {
        int n = A.size();
        int i = 1;
        
        while(i < n and A[i-1] < A[i])
            i++;
        
        if(i==n || i == 1)
            return false;
        
        while(i < n and A[i-1] > A[i])
            i++;
        
        return i == n;
    }
};