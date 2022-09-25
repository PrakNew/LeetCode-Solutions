/*
Time complexity : O(n)
Space complexity: O(1)
*/
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    int minDominoRotations(vector<int>& A, vector<int>& B) {
        int top = A[0], bot = B[0], top1 = 0, top2 = 0, bot1 = 0, bot2 = 0;
        int n = A.size();
        for(int i = 0; i < n; ++i){
            if(A[i] != top and B[i] != top)
                top = 0;
            if(A[i] != bot and B[i] != bot)
                bot = 0;
            
            top1 += A[i] == top;
            bot1 += B[i] == top;
            
            top2 += A[i] == bot;
            bot2 += B[i] == bot;
        }
        
        return (top || bot) ? min(n - max(top1, bot1), n - max(top2, bot2)): -1;
    }
};