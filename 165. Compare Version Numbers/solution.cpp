/*
Idea: Traverse dot-by-dot in each string and compare the numbers. 

Time complexity : O(n)
Space complexity: O(1)

*/

class Solution {
public:
    int compareVersion(string version1, string version2) {
        int i, j, m, n, number1, number2;
        i = j = 0;
        m = version1.size();
        n = version2.size();
        
        while(i < m || j < n){

            number1 = number2 = 0;

            while(i < m and version1[i] != '.'){
                number1 *= 10;
                number1 += version1[i] - '0';
                i++;
            }
            
            while(j < n and version2[j] != '.'){
                number2 *= 10;
                number2 += version2[j] - '0';
                j++;
            }
            
            if(number1 > number2)
                return 1;
            if(number1 < number2)
                return -1;
            
            number1 = number2 = 0;
            i++; 
            j++;
        }
        
        return 0;
    }
};