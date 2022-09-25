import collections

class Solution:
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(lambda: collections.defaultdict(int))
        
        for u, v, w in times:
            graph[u][v] = w
        
        q = collections.deque([(K, 0)])
        visited = collections.defaultdict()

        while q:
            node, time = q.popleft()
            if node not in visited:
                visited[node] = time
            else:
                visited[node] = min(visited[node], time)
            
            for nei in graph[node]:
                if nei not in visited:
                    q.append((nei, time + graph[node][nei]))
                elif nei in visited and visited[nei] > (time + graph[node][nei]):
                    q.append((nei, time + graph[node][nei]))
                    

        if len(visited)!=N:
            return -1
        
        return max(val for key, val in visited.items())
        
        