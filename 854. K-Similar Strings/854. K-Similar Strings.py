"""
Idea: BFS 

"""
import collections

class Solution:
    def kSimilarity(self, A, B):
        if A == B:
            return 0
        
        n = len(A)
        q = collections.deque([A])
        visited = set([A])
        res = 0
        
        def swap(state, i, j):
            state = [ch for ch in state]
            state[i], state[j] = state[j], state[i]
            return ''.join(state)
        
        
        while q:
            res += 1
            size = len(q)
            
            while size:
                state = q.popleft()
                i = 0
                while state[i] == B[i]:
                    i += 1
                
                for j in range(i + 1, n):
                    if state[j] == B[j] or state[j] != B[i]:
                        continue
                    
                    # swap i and j
                    new = swap(state[:], i, j)
                    
                    if new == B:
                        return res
                    
                    q += new,
                    visited.add(new)
                
                size -= 1
        