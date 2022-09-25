'''
Idea: Do BFS starting from the given matrix. At every step find all  
      possible states the matrix could reach from current state.

Time complexity : O(mn*2^mn)
Space complexity: O(2^mn)
'''

import collections

class Solution:
    def minFlips(self, A):
        m, n = len(A), len(A[0])
        
        def encode(A):
            '''  Convert matrix to string  '''
            res = ""
            for i in range(m):
                for j in range(n):
                    res += str(A[i][j]) 
            return res
        
        def decode(string):
            '''  Convert string to matrix  '''
            k = 0
            mat = [[None for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    mat[i][j] = int(string[k])
                    k += 1
            return mat
        
        def check(string):
            for ch in string:
                if ch!='0': 
                    return False
            return True
        
        def flipCell(mat, i, j):
            new_mat = [x[::] for x in mat[::]]
            new_mat[i][j] = 1 - new_mat[i][j]
            if i>0: new_mat[i-1][j] = 1 - new_mat[i-1][j]
            if i<m-1: new_mat[i+1][j] = 1 - new_mat[i+1][j]
            if j>0: new_mat[i][j-1] = 1 - new_mat[i][j-1]
            if j<n-1: new_mat[i][j+1] = 1 - new_mat[i][j+1]
            return new_mat
        
        def flip(mat):
            next_states = []
            for i in range(m):
                for j in range(n):
                    next_states += flipCell(mat, i, j),
            return next_states
        
        string = encode(A)
        q = collections.deque([(string, 0)])
        visited = set([string])
        
        while q:
            string, dist = q.popleft()
            mat = decode(string)
            
            if check(string):
                return dist
            
            for neighbor in flip(mat):
                neighbor_string = encode(neighbor)
                if neighbor_string not in visited:
                    visited.add(neighbor_string)
                    q.append((neighbor_string, dist+1))
        
        return -1