/*
Idea: Vertical Scanning 

Time complexity: O(S)
Space complexity: O(1)
*/

#include<string>
#include<vector>
using namespace std;


class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        if(n == 0)
            return "";
        string res = "";
        int j = 0;

        while(1){
            if(j == strs[0].size())
                return res;
            char ch = strs[0][j];
            for(int i = 1; i < n; ++i){
                if(j == strs[i].size() || strs[i][j] != ch)
                    return res;
            }
            res += ch;
            j++;
        }
        
        return res;
    }
};