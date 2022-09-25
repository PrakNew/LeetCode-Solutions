'''
Time complexity : O(n)
Space complexity: O(n)
'''

import collections

class Solution:
    def minimumSemesters(self, n, relations):
        graph = collections.defaultdict(list)
        inDegree = collections.defaultdict(int)
        for x, y in relations:
            graph[x] += y,
            inDegree[y] += 1
            
        visited = set()
        q = collections.deque()
        # Start BFS from courses with no prerequisites
        for i in range(1, n+1):
            if inDegree[i]==0:
                q.append(i)
                visited.add(i)
       
        semester = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        inDegree[nei] -= 1
                        if inDegree[nei] == 0: # add course with no more prerequisites
                            q.append((nei))
                            visited.add(nei)
            semester += 1       # Finished a set of courses with no prerequisites
    
        return semester if len(visited)==n else -1
                    
        