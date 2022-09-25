"""
Idea: BFS 

Time complexity : O(V + E)
Space complexity: O(E)
"""
import collections

class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        
        graph = collections.defaultdict(list)
        
        for node, head in enumerate(manager):
            graph[head] += node,
        
        q = collections.deque([(headID, informTime[headID])])
        res = float('-inf')
        
        while q:
            node, time = q.popleft()
            res = max(res, time)
            
            for nei in graph[node]:
                q += (nei, time + informTime[nei]),
        
        return res