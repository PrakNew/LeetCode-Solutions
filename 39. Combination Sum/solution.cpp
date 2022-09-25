/*
    Time complexity : O(2^n)
    Space complexity : O(2^n)
*/

class Solution {
    void util(vector<int> &candidates, int index, int rem, vector<int> &path, vector<vector<int>> &res){
            if(rem == 0){
                res.push_back(path);
                return;
            }
            
            // Backtrack if necessary
            if(index >= candidates.size() || rem < 0)
                return;
        
        
            // include current index
            path.push_back(candidates[index]);
            util(candidates, index, rem - candidates[index], path, res);
            
            // exclude current index
            path.pop_back();
            util(candidates, index + 1, rem, path, res);
        }
    
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        int n = candidates.size();
        vector<int> path;
        util(candidates, 0, target, path, res);
        return res;
    }
};