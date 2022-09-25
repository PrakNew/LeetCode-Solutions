/*
Idea: Split the array into left and right halves. Recur in accordance to their 
        range.

Time complexity: O(log n)
Space complexity: O(1)

*/

#include<vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& A, int target) {
        int n = A.size();
        int lo = 0, hi = n - 1;
        
        while(lo <= hi){
            int mid = (lo + hi) >> 1;
            
            if(A[mid] == target)
                return mid;
            
            // Check if first half is sorted
            if(A[lo] <= A[mid]){
                // Check for range
                if(A[lo] <= target and target <= A[mid])
                    hi = mid - 1;
                else
                    lo = mid + 1;
            }
            
            // Second half is sorted, check for range
            else if(A[mid] <= target and target <= A[hi])
                lo = mid + 1;
            
            // Recur to left excluding mid
            else    
                hi = mid - 1;
        }
        
        return -1;
    }
};