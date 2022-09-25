/*
Idea: Use two pointers and update the pointers by their magnitude.

Time complexity : O(n)
Space complexity: O(1)
*/

class Solution {
public:
    int maxArea(vector<int>& A) {
        int n = A.size();
        int i = 0, j = n-1;
        int max_area = INT_MIN, area;
        
        while(i < j){
            // Height * Width
            area = min(A[i], A[j]) * (j - i);
            
            max_area = max(area, max_area);
            
            if(A[i] < A[j])
                i++;
            else
                j--;
        }
        
        return max_area;
    }
};