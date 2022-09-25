'''
Classic DP problem with space optimization. We need information about just two rows at any instance of time.
Just maintain two rows of information instead of matrix.

Time complexity : O(mn)
Space complexity: O(n)

'''

class Solution(object):
    def maximalSquare(self, A):
        if A == []:
            return 0
        m, n = len(A), len(A[0])
        first, second = [0] * (n+1), [0] * (n+1)
        max_side = 0
        
        for i in range(m):
            for j in range(n):
                second[j] = 1 if A[i][j] == '1' else 0
                if i>0 and j>0 and second[j]:
                    second[j] = min(second[j-1], first[j], first[j-1]) + 1
                max_side = max(max_side, second[j])
            first = second[::]
            
        return max_side * max_side