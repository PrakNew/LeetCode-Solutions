/*
    Time complexity : O(n)
    Space complexity: O(n)
*/

#include<map>
#include<deque>
#include<algorithm>

using namespace std;

class Solution {
public:
    string removeDuplicateLetters(string s) {
        int n = s.size();
        map<int, int> hash;
        deque<char> st;
        
        for(int i = 0; i < n; ++i)
            hash[s[i]] = i;
        
        for(int i = 0; i < n; ++i){
            if(find(begin(st), end(st), s[i]) != end(st))
                continue;
            while(!st.empty() and s[i] < st.back() and hash[st.back()] > i)
                st.pop_back();
            st.push_back(s[i]);
        }
        
        string res = "";
        for(auto ch: st)
            res += ch;
        
        return res;
    }
};