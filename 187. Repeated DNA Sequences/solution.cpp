/*
Idea: Use rolling hash technique to compute the hash of each window at each iteration. 
     Check if the hash already exists/
    
Time complexity : O(n)
Space complexity: O(n)
*/

#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<cmath>
using namespace std;

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        int n = s.size();
        int prime = 3;
        int m = 10;
        map<long, string> seen;
        vector<string> res;
        set<string> res_set;
        string text = s.substr(0, m);
        long textHash = computeHash(text, prime);
        seen[textHash] = text;
        
        for(int i = 1; i <= n - m; ++i){
            // update rolling hash
            textHash -= s[i-1];
            textHash /= prime;
            textHash += s[i+m-1] * pow(prime, m-1);
            text = s.substr(i, m);
            
            // check for matching hash
            if(seen.find(textHash) != seen.end() and seen[textHash] == text)
                res_set.insert(text);

            seen[textHash] = text;
        }
        
        for(auto text: res_set)
            res.push_back(text);
        
        return res;
    }
private:
    long computeHash(string text, int prime){
        long hash = 0;
        int m = text.size();
        for(int i = 0; i < m; ++i){
            hash += text[i] * pow(prime, i);
        }
        
        return hash;
    }
};