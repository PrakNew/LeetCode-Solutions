/*
Idea: Backtracking

Time complexity : O(4^n / sqrt(n) )
Space complexity: O(4^n / sqrt(n) )
*/
#include<vector>
#include<string>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        util(n, n, "", res);
        return res;
    }
private:
    void util(int left, int right, string s, vector<string>& res){
        if(right == 0){
            res.push_back(s);
            return;
        }
        
        if(left || left == right)
            util(left - 1, right, s + '(', res);
        if(left < right)
            util(left, right - 1, s + ')', res);
    }
};