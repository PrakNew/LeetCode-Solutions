/*
Idea: Binary search with slight modification: while checking for mid, simultaneously 
      check for mid + 1 position as well.

Time complexity: O(log N)
Space complexity: O(1)
*/


#include<vector>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& A) {
        int n = A.size();
        int lo = 0, hi = n - 1;
        
        if(A[lo] < A[hi])
            return A[lo];
        
        
        while(lo <= hi){
            int mid = (lo + hi) >> 1;
            
            // Check if mid is target
            if(check(A, mid))
                return A[mid];
            
            // Check if mid + 1 is target
            if(mid < n-1 and check(A, mid + 1))
                return A[mid+1];
            
            if(A[lo] < A[mid])
                lo = mid + 1;
            else
                hi = mid - 1;
        }
        
        return -1;
    }
private:
    bool check(vector<int>& A, int x){
        int n = A.size();
        return (x==0 || A[x-1] > A[x]) and (x == n-1 or A[x] < A[x+1]);
    }
};