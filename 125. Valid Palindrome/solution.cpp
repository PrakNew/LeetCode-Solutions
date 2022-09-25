/*
Time complexity: O(n)
Space complexity: O(1)
*/

#include<string>
using namespace std;


class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.size();
        
        if(n <= 1)
            return true;
        
        int i = 0, j = n - 1;
        char ch1, ch2;
        
        while(i < j){
            while(i < j and !isalnum(s[i]))
                i++;
            
            while(i < j and !isalnum(s[j]))
                j--;
            
            if(i == j)
                break;
            
            if(isdigit(s[i]) and isdigit(s[j]) and s[i] != s[j])
                return false;
            
            ch1 = s[i];
            ch2 = s[j];
            
            if(isupper(s[i]))
                ch1 |= ' ';
            
            if(isupper(s[j]))
                ch2 |= ' ';
            
            if(ch1 != ch2)
                return false;
            
            i++;
            j--;
        }
        
        return true;
    }
};