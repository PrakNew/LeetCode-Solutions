/*
Idea: Extend two pointers with another pointer.

Time complexity : O(n^2)
Space complexity: O(1)
*/

#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& A) {
        int n = A.size();
        sort(begin(A), end(A));
        vector<vector<int>> res;
        int k = 0, i, j, target, sum, prev;
        
        for(k = 0; k < n; ++k){
            
            // Three positive numbers cannot sum to 0
            if(A[k] > 0)
                break;
            
            target = -A[k];
            
            i = k + 1;
            j = n - 1;
            
            // Avoid duplicates
            if(k > 0 and A[k] == A[k-1])
                continue;
            
            // Two sum with given target
            while(i < j){
                sum = A[i] + A[j];

                if(sum == target){
                    res.push_back({A[k], A[i], A[j]});
                    
                    // Avoid duplicates
                    prev = A[i];
                    while(i < j and A[i] == prev)
                        i++;
                    
                    prev = A[j];
                    while(i < j and A[j] == prev)
                        j--;
                }
                
                else if(sum > target)
                    j--;
                
                else
                    i++;
            }
        }
        
        return res;
    }
};