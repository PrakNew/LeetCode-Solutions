/*
    Time complexity : O(n log n)
    Space complexity: O(1)
*/

#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    int twoSumLessThanK(vector<int>& A, int K) {
        int n = A.size();
        int max_s = -1, j;
        sort(A.begin(), A.end());
    
        for(int i = 0; i < n and A[i] < K; ++i){
           j = lower_bound(begin(A), end(A), K - A[i]) - begin(A) - 1;
           if(i < j)
               max_s = max(max_s, A[i] + A[j]);
        }
        
        return max_s;
    }
};