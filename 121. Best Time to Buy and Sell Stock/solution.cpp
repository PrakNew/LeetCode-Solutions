/*
    Time complexity : O(n)
    Space complexitY: O(1)
*/

#include<vector>
#include<climits>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_buy = INT_MAX, profit = 0;
        
        for(int i = 0; i < prices.size(); ++i){
            min_buy = min(min_buy, prices[i]);
            profit = max(profit, prices[i] - min_buy);
        }
        return profit;
    }
};