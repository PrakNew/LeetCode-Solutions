'''
Idea: Since all the elements are in the range 1<=A[i]<=n, use array as hash map

Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def findDisappearedNumbers(self, A):
        n = len(A)
        res = []
        for i in range(n):
            ind = abs(A[i]) - 1
            if A[ind] > 0:
                A[ind] *= -1
        
        for i in range(n):
            if A[i]>0:
                res.append(i+1)
        
        return res