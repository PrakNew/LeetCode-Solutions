/*
Time complexity : O(n * m)
Space complexity: O(n)
*/

#include<iostream>
#include<vector>
#include<climits>
using namespace std;


class Solution {
public:
    vector<string> commonChars(vector<string>& A) {
        int n = A.size();
        int mp[26][100] = {0};
        vector<string> res;
        for(int i = 0; i < n; ++i){
            for(char ch: A[i]){
                mp[ch-'a'][i]++;
            }
        }
        for(int i = 0; i < 26; ++i){
            int ct = INT_MAX;
            for(int j = 0; j < n; ++j)
                ct = min(ct, mp[i][j]);
            while(ct--){
                string s(1, 'a'+i);
                res.push_back(s);
            }
        }
        return res;
    }
};