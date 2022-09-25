#include<vector>
using namespace std;

struct S{
  int start;
  int end;
  S(int s, int e){
      start = s;
      end = e;
  }
};

bool comparator(struct S a, struct S b){
    return a.end < b.end;
}

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int n = intervals.size();
        if(n==0)
            return 0;
        
        vector<S> v;
        for(auto interval : intervals)
            v.push_back(S(interval[0], interval[1]));
        
        sort(begin(v), end(v), comparator);
        
        int res = 0, prev =  v[0].end;
        for(int i = 1; i < n; ++i){
            if(v[i].start < prev)
                res++;
            else
                prev = v[i].end;
        }
        return res;
    }
};