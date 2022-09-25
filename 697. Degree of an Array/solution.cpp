#include<vector>
#include<map>

using namespace std;

class Solution {
public:
    int findShortestSubArray(vector<int>& A) {
        int n = A.size();
        int degree = 0;
        map<int, int> left;
        map<int, int> right;
        map<int, int> count;
        
        for(int i = 0; i < n; ++i){
            if(count.find(A[i]) == count.end())
                left[A[i]] = i;
            
            right[A[i]] = i;
            count[A[i]]++;
            degree = max(degree, count[A[i]]);
        }
        
        int res = n;
        
        for(auto item: count){
            int x = item.first;
            if(count[x] == degree)
                res = min(res, right[x] - left[x] + 1);
        }
        
        return res;
    }
};