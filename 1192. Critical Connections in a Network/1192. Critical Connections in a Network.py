'''

Idea: Use Bridges algorithm to find the bridges in the given graph. 
      Bridges are defined as the edges whose removal increases the
      number of connected components.

Time complexity : O(V+E)
Space complexity: O(V+E)
'''

import collections 

class Solution:
    def criticalConnections(self, n, connections):

        graph = collections.defaultdict(list)
        for a, b in connections:
            graph[a] += b,
            graph[b] += a,
        
        bridges = []
        ids = [None] * n
        low = [None] * n
        self.label = 0
        
        def dfs(node, parent):
            if ids[node] is None:
                ids[node] = low[node] = self.label
                self.label += 1
                for nei in graph[node]:
                    if ids[nei] is None:
                        dfs(nei, node)
                
                if parent is None:
                    low[node] = min([low[i] for i in graph[node]] + [low[node]])
                else:
                    low[node] = min([low[i] for i in graph[node] if i!=parent] + [low[node]])
            

        dfs(0, None)        
        for edge in connections:
            a, b = edge
            if ids[a] < low[b] or ids[b] < low[a]:
                bridges += [a, b],
        
        return bridges