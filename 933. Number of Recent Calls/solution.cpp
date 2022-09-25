#include<iostream>
#include<deque>

using namespace std;


class RecentCounter {
public:
    deque<int> queue;
    int size;
    
    RecentCounter() {
        this->size = 0;    
    }
    
    int ping(int t) {
        while(this->queue.size() && this->queue.front() < t-3000){
            this->queue.pop_front();
            this->size--;
        }
        this->queue.push_back(t);
        this->size++;
        return this->size;
    }
};