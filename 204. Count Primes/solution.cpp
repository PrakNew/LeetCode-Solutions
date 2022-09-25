/*
Time complexity : O(n log log n)
Space complexity: O(n)
*/

#include<vector>
using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        if(n <= 2)
            return 0;
        
        vector<int> primes(n , 1);
        primes[0] = primes[1] = 0;
        
        for(int i = 2; i*i < n; i++){
            if(primes[i]){
                for(int p = i * i; p < n; p += i)
                    primes[p] = 0;
            }
        }
        
        int res = 0;
        
        for(auto x: primes)
            res += x == 1;
        
        return res;
    }
};