/*
Time complexity : O(n log n) 
Space complexity: O(1)

*/

#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return constantSpace(nums);
    }
private:
  bool constantSpace(vector<int>& A){
      int n = A.size();
      sort(begin(A), end(A));
      for(int i = 1; i < n; ++i)
          if(A[i] == A[i-1])
              return true;
      return false;
  }  
  bool linearTime(vector<int>& A){
      set<int> seen;
      int n = A.size();
      for(int i = 0; i < n; ++i){
          if(seen.count(A[i]))
              return true;
          seen.insert(A[i]);
      }
      return false;
  }
};