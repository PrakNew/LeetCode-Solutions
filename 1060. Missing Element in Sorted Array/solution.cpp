/*
    Idea: Find the leftmost element such that 
            missing(pos-1) < k <= missing(pos)
            
    Time complexity : O(log n)
    Space complexity: O(1)
*/
#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int missingElement(vector<int>& A, int k) {
        int n = A.size();
        int lo, hi, mid;
        
        if(missing(A, n-1) < k)
            return A[n-1] + k - missing(A, n-1);
        
        lo = 0;
        hi = n-1;
        while(lo < hi){
            mid = (lo + hi) >> 1;
            
            if(missing(A, mid) < k)
                lo = mid + 1;
            else
                hi = mid;
        }
        return A[lo-1] + k - missing(A, lo-1);
    }

private:
    int missing(vector<int> A, int x){
        return A[x] - A[0] - x;
    }
        
};