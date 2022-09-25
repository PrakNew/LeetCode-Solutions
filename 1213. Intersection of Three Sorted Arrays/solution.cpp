/*
Idea: Merge sort technique

Time complexity : O(n + m + o)
Space complexity: O(n + m + o)
*/
#include<vector>
using namespace std;


class Solution {
public:
    vector<int> arraysIntersection(vector<int>& arr1, vector<int>& arr2, vector<int>& arr3) {
        int m = arr1.size(), n = arr2.size(), o = arr3.size();
        int i = 0, j = 0, k = 0;
        vector<int> res;
        while(i < m and j < n and k < o){
            if(arr1[i] == arr2[j] and arr2[j] == arr3[k]){
                res.push_back(arr1[i]);
                i++; j++; k++;
            }
            
            else if(arr1[i] == min(arr1[i], min(arr2[j], arr3[k])))
                i++;
            else if(arr2[j] == min(arr1[i], min(arr2[j], arr3[k])))
                j++;
            else
                k++;
        }
        return res;
    }
};