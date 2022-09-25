'''
Idea: Since all the elements are in the range 1<=A[i]<=n, use array as hash map

Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def findDuplicates(self, A):
        res = []
        n = len(A)
        for i in range(n):
            ind = abs(A[i])-1 # fetch the index pointed by current element
            if A[ind] < 0:    # already visited
                res += abs(A[i]),
            else:             # not visited before
                A[ind] *= -1  

        return res
        
        