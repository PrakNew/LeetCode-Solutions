"""
Idea: Maintain two graphs and perform BFS choosing nodes alternatively 
        from both the graphs

"""

import collections

class Solution:
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        res = [-1] * n
        res[0] = 0
        graph_red = collections.defaultdict(list)
        graph_blue = collections.defaultdict(list)
        
        # color : 1 - red and 0 - blue
        q = collections.deque()
        visited = set()
        
        for a, b in red_edges:
            graph_red[a] += b,
            if a == 0:
                q += (b, 1, 1),
                visited.add((b, 1))
        
        for a, b in blue_edges:
            graph_blue[a] += b,
            if a == 0:
                    q += (b, 0, 1),
                    visited.add((b, 0))
        
        while q:
            node, color, dist = q.popleft()
            
            if res[node] == -1:
                res[node] = dist

            if color == 1:
                for nei in graph_blue[node]:
                    if (nei, 0) not in visited:
                        q += (nei, 1 - color, dist + 1),
                        visited.add((nei, 0))
            
            if color == 0:
                for nei in graph_red[node]:
                    if (nei, 1) not in visited:
                        q += (nei, 1 - color, dist + 1),
                        visited.add((nei, 1))
            
        return res

