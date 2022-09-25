/*
    Idea: Starting processing both the arrays from back

    Time complexity : O(n)
    Space complexity: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Start filling from back
        int k = nums1.size() - 1;
        int i = m - 1, j = n - 1;
        
        while(i >= 0 and j >= 0){
            if(nums1[i] > nums2[j])
                nums1[k--] = nums1[i--];
            else
                nums1[k--] = nums2[j--];
        }
        
        while (i >= 0)
            nums1[k--] = nums1[i--];
        while(j >= 0)
            nums1[k--] = nums2[j--];    
    }
};