'''
Idea: Draw edges between stop and buses. Perform BFS starting from S.

Time complexity: O(n^2)
Space complexity: O(n^2)

'''

import collections

class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T: 
            return 0
        
        graph = collections.defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop] += bus,
        

        visited = set()
        res = 0
        q = collections.deque([S])
        while q:
            size = len(q)
            for _ in range(size):
                curr_stop = q.popleft()
                if curr_stop == T:
                    return res
                for bus in graph[curr_stop]:
                    if bus not in visited:
                        visited.add(bus)
                        for stop in routes[bus]:
                            q.append(stop)
            res += 1
            
        return -1