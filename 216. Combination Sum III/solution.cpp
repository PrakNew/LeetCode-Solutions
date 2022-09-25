class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int> > res;
        vector<int> path;
        util(1, n, path, res, k);
        return res;
    }
private:
    void util(int digit, int rem, vector<int> &path, vector<vector<int> > &res, int k){
        
        if(rem==0 && path.size() == k){
            res.push_back(path);
            return;
        }
        
        if(rem < 0 || path.size() > k)
            return;
        
        for(int i = digit; i < 10 && i <= rem; ++i){
            path.push_back(i);
            util(i + 1, rem - i, path, res, k);
            path.pop_back();
        }
    }
};