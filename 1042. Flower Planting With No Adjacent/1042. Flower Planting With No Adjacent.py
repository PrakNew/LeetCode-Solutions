import collections

class Solution:
    def gardenNoAdj(self, N, paths):
        # 1. Find color of neighbors
        # 2. From that set, we can find the color of the node
        
        graph = collections.defaultdict(list)
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)
        
        colors = [0] * (N+1)
        
        for node in range(1, N+1):
            nei_colors = set()
            for nei in graph[node]:
                nei_colors.add(colors[nei])
            for k in range(1, 5):
                if k not in nei_colors:
                    colors[node] = k
                    break
        
        return colors[1:]
        