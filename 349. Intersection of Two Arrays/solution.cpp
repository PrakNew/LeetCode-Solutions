/*
Idea: Create two sets, and time complexity of contains operation in set is O(1)

Time complexity: O(n + m)
Space complexity: O(n + m)
*/

#include<vector>
#include<unordered_set>
using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& A, vector<int>& B) {
        unordered_set<int> st1(begin(A), end(A));
        unordered_set<int> st2(begin(B), end(B));
        vector<int> res;
        for(auto x: st2)
            if(st1.count(x))
                res.push_back(x);
        return res;
    }
};