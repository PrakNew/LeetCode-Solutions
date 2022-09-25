/*
Time complexity : O(n * m)
Space complexity: O(n * m)
*/

#include<vector>
#include<map>
#include<string>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> mp;

        for(auto str: strs){
            vector<int> mask(26, 0);
            for(auto ch: str)
                mask[ch-'a']++;
            mp[mask].push_back(str);
        }
        
        vector<vector<string>> res;
        
        for(auto it: mp)
            res.push_back(it.second);
        
        return res;
    }
};