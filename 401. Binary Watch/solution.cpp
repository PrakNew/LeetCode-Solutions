/*
    Time complexity : O(1)
    Space complexity: O(1)
*/
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<string> readBinaryWatch(int num) {
        vector<string> res;   
        for(int hr = 0; hr <= 11; ++hr){
            for(int min = 0; min <= 59; ++min){
                int hr_bits = __builtin_popcount(hr);
                int min_bits = __builtin_popcount(min);
                if(hr_bits + min_bits == num) {
                    if(min <= 9)
                        res.push_back(to_string(hr) + ":0" + to_string(min));
                    else
                        res.push_back(to_string(hr) + ":" + to_string(min));
                }
            }
        }
        return res;
    }
};