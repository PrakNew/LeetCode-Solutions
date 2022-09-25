/*
    Time complexity : O(n)
    Space complexity: O(n)
*/

#include<vector>
#include<set>
using namespace std;

class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        set<float> seen;
        int n = arr.size();
        for(int i = 0; i < n; ++i){
            if(seen.count(arr[i] * 2.0) == 1 || seen.count(arr[i]/2.0) == 1)
                return true;
            seen.insert(arr[i] * 1.0);
        }
        return false;
    }
};