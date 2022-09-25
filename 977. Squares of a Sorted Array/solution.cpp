/*

Idea: Use two pointers approach one for each positive and negative numbers. Use merge sort like algorithm to advance the pointers.

Time complexity : O(n)
Space complexity: O(n)
*/

class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        int n = A.size();
        
        vector<int> squares(n);
        if(n==1){
            return {A[0] * A[0]};
        }
        int j = -1;
        for(int i = 0; A[i] < 0 and i < n; ++i){
            j = i;
        }
        
        if(j==-1){ // no negative elements
            for(int i = 0; i < n; ++i)
                squares[i] = A[i] * A[i];
        }
        else{
            int i = j + 1;
            int k = 0;
            // Similar to merge sort
            while(j >=0 and i < n){
                if(abs(A[i]) < abs(A[j]))
                    squares[k++] = A[i] * A[i++];
                else
                    squares[k++] = A[j] * A[j--];
            }
            
            while(j>=0)
                squares[k++] = A[j] * A[j--];
            
            while(i<n)
                squares[k++] = A[i] * A[i++];
        }
        
        return squares;
    }
        
};