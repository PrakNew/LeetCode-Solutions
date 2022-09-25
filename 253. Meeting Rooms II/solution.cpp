/*
Idea: Sort based on the starting times. Maintain a heap of occupied rooms based on end times. Remove a room as soon 
      its end time is less than current start time. In this fashion, the maximum number of occupied rooms is indicated 
      by the maximum size of heap.

Time complexity : O(n log n)
Space complexity: O(n)
*/

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std; 

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if(intervals.empty())
            return 0;
       
        sort(begin(intervals), end(intervals)); 

        vector<int> heap;
        heap.push_back(-intervals[0][1]);
        make_heap(begin(heap), end(heap));
        
        int max_rooms = 1;
    
        for(int i = 1; i < intervals.size(); ++i){
            while(heap.size() and -heap.front() <= intervals[i][0]){
                pop_heap(begin(heap), end(heap));
                heap.pop_back();
            }
            
            heap.push_back(-intervals[i][1]);
            push_heap(begin(heap), end(heap));

            if(heap.size() > max_rooms)
                max_rooms = heap.size();
        }
        
        return max_rooms;
    }
};