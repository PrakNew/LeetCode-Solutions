#include<iostream>

using namespace std;

class Solution {
public:
    bool buddyStrings(string A, string B) {
        if(A.size() != B.size())
            return false;
        
        if(A == B){
            int mp[26] = {0};
            for(auto ch: A){
                mp[ch-'a']++;
                if(mp[ch-'a'] > 1)
                    return true;
            }
            return false;
        }
        else{
            int first, second;
            first = second = -1;
            for(int i = 0; i < A.size(); ++i){
                if(A[i] != B[i]){
                    if(first == -1) 
                        first = i;
                    else if(second == -1)
                        second = i;
                    else
                        return false;
                }
            }
            return second != -1 and A[first] == B[second] and A[second] == B[first];
        }
    }
};