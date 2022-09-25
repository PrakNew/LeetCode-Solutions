/*
Time complexity: O(1)
Space complexity: O(n)
*/

#include<stack>
#include<climits>
using namespace std;

class MinStack {
public:
    /** initialize your data structure here. */
    stack<long> st;
    long min;
    
    MinStack() {
        min = INT_MIN;
    }
    
    void push(int x) {
        if(st.empty()){
            st.push(x);
            min = x;
            return;
        }
        
        if(x < min){

            long new_x = (long) 2 * x - min;
            st.push(new_x);
            min = x;
        }
        else{
            st.push(x);
        }
    }
    
    void pop() {
        if(st.top() < min){
            long new_min = 2 * min - st.top();
            st.pop();
            min = new_min;
            return;
        }
        st.pop();
    }
    
    int top() {
        if(st.top() < min)
            return min;
        return st.top();
    }
    
    int getMin() {
        return min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */