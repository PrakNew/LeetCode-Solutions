/*
Idea: Backtracking

Time complexity : O(3^n * 4^m)
Space complexity: O(3^n * 4^m)
*/

#include<vector>
#include<string>
#include<map>
using namespace std;


class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if(digits.size() == 0)
            return {};
        map<int, vector<char>> mp;
        mp[2] = {'a', 'b', 'c'};
        mp[3] = {'d', 'e', 'f'};
        mp[4] = {'g', 'h', 'i'};
        mp[5] = {'j', 'k', 'l'};
        mp[6] = {'m', 'n', 'o'};
        mp[7] = {'p', 'q', 'r', 's'};
        mp[8] = {'t', 'u', 'v'};
        mp[9] = {'w', 'x', 'y', 'z'};
        
        vector<string> res;
        util(0, digits, "", mp, res);
        return res;
    }
private:    
    void util(int i, string digits, string curr, map<int, vector<char>>& mp, vector<string>& res){
        if(i == digits.size()){
            res.push_back(curr);
            return;
        }
        
        for(auto ch: mp[digits[i] - '0'])
            util(i + 1, digits, curr + ch, mp, res);
    }
};