/*
Time complexity : O(n)
Space complexity: O(n)
*/

class Solution {
public:
    int findPairs(vector<int>& A, int k) {
        int n = A.size();
        map<int, int> counter;
        int res = 0;
        
        for(auto x: A)
            counter[x]++;
 
        map<int, int>::iterator it;
        
        for(it = counter.begin(); it != counter.end(); ++it){
            if((k==0 and it->second >= 2) || (k > 0 and counter.find(it->first + k) != counter.end()))
               res ++;
        }
        return res;
    }
};