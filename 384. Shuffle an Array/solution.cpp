/*
Idea: Fisher Yates algorithm

    Time complexity: O(n)
    Space complexity: O(n)
*/
#include<vector>
#include<climits>
using namespace std;

class Solution {
    vector<int> A;
public:
    
    Solution(vector<int>& nums) {
        A = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return A;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> res(begin(A), end(A));
        for(int i = 0; i < res.size(); ++i){
            int idx = rand() % res.size();
            swap(&res[i], &res[idx]);
        }
        return res;
    }

private:
    
    void swap(int* a, int* b){
        int temp = *a;
        *a = *b;
        *b = temp;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */