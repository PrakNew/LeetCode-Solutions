/*

Idea: Maintain a sorted list using binary search for inserting new elements. 
      Use two pointers to check if any two numbers sum to target
    

Time complexity : O(n log n)
Space complexity: O(n)
*/

#include<vector>
#include<algorithm>

using namespace std;


class TwoSum {
public:
    /** Initialize your data structure here. */
    vector<int> q;
    TwoSum() {
        
    }
    
    /** Add the number to an internal data structure.. */
    void add(int number) {
        int pos = lower_bound(begin(q), end(q), number) - begin(q);
        q.insert(begin(q) + pos, number);
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    bool find(int value) {
        int lo = 0, hi = q.size()-1;
        while(lo < hi){
            int curr_sum = q[lo] + q[hi];
            if(curr_sum == value)
                return true;
            else if(curr_sum < value)
                lo++;
            else
                hi--;
        }
        return false;
    }
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */