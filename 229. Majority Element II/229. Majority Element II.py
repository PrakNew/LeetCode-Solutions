'''
Idea: Use Boyer-Moore voting algorithm to find numbers that appear more than floor(n/k) times. 

First pass:
1. If counter is 0, vote the current number to be the candidate
2. If current number is same as candidiate, increment counter otherwise decrement

Second pass:
1. Check if occurences of the candidates are more than n/k times

Time complexity : O(n)
Space complexity: O(1)

'''

class Solution:
    def majorityElement(self, A):
        n = len(A)
        if n == 0:
            return []
        k = 3
        ct1 = ct2 = 0
        candidate1 = candidate2 = None
        
        for x in A:
            if candidate1==x:
                ct1 += 1
            elif candidate2==x:
                ct2 += 1
            elif ct1==0:
                candidate1 = x
                ct1 += 1
            elif ct2==0:
                candidate2 = x
                ct2 += 1
            else:
                ct1-=1
                ct2-=1
        
        ct1 = ct2 = 0
        
        for x in A:
            if x==candidate1:
                ct1 += 1
            elif x==candidate2:
                ct2 += 1
        
        res = [] 
        
        if ct1 > n//k:
            res.append(candidate1)
        
        if ct2 > n//k:
            res.append(candidate2)
                
        return res
        