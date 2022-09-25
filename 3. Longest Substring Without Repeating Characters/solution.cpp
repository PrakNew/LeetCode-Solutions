/*
Time complexity : O(n)
Space complexity: O(1)
*/

#include<vector>
#include<string>
using namespace std;


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        vector<int> window(128, 0);
        int i = 0, j = 0, n = s.size();
        while(j < n){
            while(window[s[j]])
                window[s[i++]]--;
           
            window[s[j++]]++;
            int ct = 0;
            
            for(int p = 0; p < 128; ++p)
                ct += window[p];
            
            res = max(res, ct);
        }
        
        return res;
    }
};