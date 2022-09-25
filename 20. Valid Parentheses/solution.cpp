/*
Time complexity : O(n)
Space complexity: O(n)
*/

#include<stack>
#include<string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(auto x: s){
            if(x == '(' || x == '{' || x == '[')
                st.push(x);
            else if(x == ')'){
                if(st.empty() || st.top() != '(')
                    return false;
                st.pop();
            }
            else if(x == ']'){
                if(st.empty() || st.top() != '[')
                    return false;
                st.pop();
            }
            else if(x == '}'){
                if(st.empty() || st.top() != '{')
                    return false;
                st.pop();
            }
        }
        return st.empty();
    }
};