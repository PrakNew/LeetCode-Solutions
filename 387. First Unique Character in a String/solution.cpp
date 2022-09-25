/*
Time complexity: O(n)
Space complexity: O(1)
*/

#include<string>
using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        int n = s.size();
        int last[26] = {0};  // only 26 letters

        for(int i = 0; i < n; ++i)
            last[s[i] - 'a']++;
        
        for(int i = 0; i < n; ++i)
            if(last[s[i] - 'a'] == 1)
                return i;

        return -1;
    }
};