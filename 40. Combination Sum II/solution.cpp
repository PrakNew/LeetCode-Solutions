#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& A, int target) {
        vector<vector<int>> res;
        sort(A.begin(), A.end());
        vector<int> path;
        int n = A.size();
        util(A, 0, target, path, res, target);
        return res;
    }
    
private:
    void util(vector<int> &A, int index, int rem, vector<int> &path, vector<vector<int> > &res, int target){
        
        if(rem == 0){
            sort(path.begin(), path.end());
            if(find(res.begin(), res.end(), path) == res.end()){
                res.push_back(path);
            }
            return;
        }
    
        for(int i = index; i < A.size() && A[i] <= rem; ++i){
            path.push_back(A[i]);
            util(A, i+1, rem - A[i], path, res, target);
            path.pop_back();
        }
    }
};