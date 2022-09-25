'''
Idea: By Boyer-Moore intuition, an element is a majority element if it appears more than n/2 times

Time complexity : O(n)
Space complexity : O(1)

'''

class Solution:
    def isMajorityElement(self, A, target):
        ct = 0
        n = len(A)
        for x in A:
            if target==x:
                ct += 1
        
        return ct > n/2
        