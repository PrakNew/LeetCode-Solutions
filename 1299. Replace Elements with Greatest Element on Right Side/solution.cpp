/*
    Time complexity : O(n)
    Space complexity: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n = arr.size(), max_so_far, temp;
        max_so_far = arr[n-1];
        arr[n-1] = -1;
        for(int i = n - 2; i >= 0; --i){
            temp = arr[i];
            arr[i] = max_so_far;
            max_so_far = max(max_so_far, temp);
        }
        return arr;
    }
};