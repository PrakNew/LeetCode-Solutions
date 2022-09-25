class Solution {
public:
    vector<int> twoSum(vector<int>& A, int target) {
        int n = A.size();
        vector<int> res(2, -1);
        int lo = 0, hi = n - 1;
        
        while(lo < hi){
            int curr_sum = A[lo] + A[hi];
            if(curr_sum == target){
                res = {lo + 1, hi + 1};
                return res;
            }
            else if(curr_sum > target)
                hi--;
            else
                lo++;
            
        }
        
        return res;
    }
};