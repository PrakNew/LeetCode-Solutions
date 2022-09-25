/* 

Time complexity : O(kn)
Space complexity: O(kn)
*/

#include<vector>
using namespace std;

class Solution {
public:
    int maxProfit(int K, vector<int>& prices) {
        int n = prices.size();
        if(n==0)
            return 0;
        
        
        // Number of transactions is more than possible transactions
        if(K > n>>1){
            int res = 0;
            for(int i = 1; i < n; ++i)
                if(prices[i] > prices[i-1])
                    res += prices[i] - prices[i-1];
            return res;
        }
        
        
        vector<vector<int>> dp(K + 1, vector<int> (n, 0));
        int buy;
        for(int k = 1; k <= K; ++k){
            buy = prices[0];
            for(int i = 1; i < n; ++i){
                buy = min(buy, prices[i] - dp[k-1][i-1]);
                dp[k][i] = max(dp[k][i-1], prices[i] - buy);
            }
        }
        
        return dp[K][n-1];
    }
};