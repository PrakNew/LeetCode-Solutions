'''
Time complexity : O(N log N)
Space complexity: O(1)

If hashmap is used:
Time complexity: O(N)
Space complexity: O(N)
'''


class Solution:
    def containsDuplicate(self, A):
        n = len(A)
        A.sort()
        for i in range(1, n):
            if A[i] == A[i-1]:
                return True
        return False