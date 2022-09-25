/*
    Time complexity : O(n)
    Space complexity: O(1)
*/

#include<vector>
using namespace std;

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int n = A.size();
        int temp, k = 0;
        for(int i = 0; i < n; ++i){
            if((A[i] & 1) == 0 ){
                temp = A[i];
                A[i] = A[k];
                A[k] = temp;
                k++;
            }
        }
        return A;
    }
};