/*
Idea: Problem boils down to a simple problem if the original array is reversed.

Time complexity : O(n)
Space complexity: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& A, int k) {
        int n = A.size();
        
        k = k % n;
        
        if(k==0)
            return;

        // Step 1: Reverse the array
        for(int i = 0; i < n>>1; ++i){
            swap(&A[i], &A[n-i-1]);
        }
        
        // Step 2: Reverse the subarray [0,...,k-1]
        for(int i = 0; i < (k >> 1); ++i){
            swap(&A[i], &A[k-i-1]);
        }
        
        // Step 3: Reverse the subarray [k,...,n-1]
        int j = n - 1;
        for(int i = k; i < j; ++i, --j){
            swap(&A[i], &A[j]);
        }
        
    }
private:
    void swap(int *a, int *b){
        int temp = *a;
        *a = *b;
        *b = temp;
    }
};