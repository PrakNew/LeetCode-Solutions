/*
Idea: Keep two variables, one each for max product and min product. Exchange the values of the 
        variables accordingly for positive and negative numbers.

Time complexity : O(n)
Space complexity: O(1)
*/

#include<vector>
#include<climits>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& A) {
        int n = A.size();
        int max_val, min_val, max_prod;
        max_val = min_val = 1;
        max_prod = INT_MIN;
        
        for(int i = 0; i < n; ++i){
            if(A[i] >= 0){
                max_val *= A[i];
                min_val *= A[i];
            }
            else {
                swap(&max_val, &min_val);
                max_val *= A[i];
                min_val *= A[i];
            }
            
            
            max_prod = max(max_val, max_prod);
            
            max_val = max(1, max_val);
            min_val = min(1, min_val);
        }
        
        return max_prod;
    }
private:
    void swap(int* a, int* b){
        int temp = *a;
        *a = *b;
        *b = temp;
    }
};

