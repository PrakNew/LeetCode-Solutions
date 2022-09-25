/*
Time complexity: O(n)
Space complexity: O(1)
*/

#include<string>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        int m = s.size(), n = t.size();
        if(m != n)
            return false;
        
        int mask1[26] = {0};
        int mask2[26] = {0};
        
        for(auto x: s)
            mask1[x - 'a']++;
        
        for(auto x: t)
            mask2[x - 'a']++;
        
        for(int i = 0; i < 26; ++i)
            if(mask1[i] != mask2[i])
                return false;
        
        return true;
    }
};