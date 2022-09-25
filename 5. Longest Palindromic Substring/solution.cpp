/*
Idea: Manacher's algorithm

Time complexity : O(n)
Space complexity: O(n)
*/

#include<vector>
#include<string>
using namespace std;


class Solution {
public:
    string longestPalindrome(string s) {
        string A = "@#";
        for(auto ch: s){
            A += ch;
            A += "#";
        }
        int n = A.size();
        vector<int> Z(n, 0);
        int center, right;
        center = right = 0;
        
        for(int i = 1; i < n - 1; ++i){
            if(i < right)
                Z[i] = min(right - i, Z[2 * center - i]);
            
            while(A[i + Z[i] + 1] == A[i - Z[i] - 1])
                Z[i]++;
            
            if(right < (i + Z[i])){
                center = i;
                right = i + Z[i];
            }
        }
        
        int maxlen = 0;
        
        for(int i = 0; i < n; ++i){
            if(Z[i] > maxlen){
                maxlen = Z[i];
                center = i;
            }
        }
        
        int l = (center - maxlen) >> 1;
        int r = (center + maxlen) >> 1;
        
        return s.substr(l, r - l);
    }
};