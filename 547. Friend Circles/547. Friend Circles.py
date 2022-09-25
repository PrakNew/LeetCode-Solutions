import collections

class Solution:
    def findCircleNum(self, M):
        if M==[]:
            return 0
        
        m, n = len(M), len(M[0])
        visited = [False] * n
        circles = 0
        
        graph = collections.defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                if M[i][j]==1:
                    graph[i].append(j)
                    graph[j].append(i)

        for i in range(n):
            if not visited[i]:
                circles += 1
                dfs = [i]
                while dfs:
                    friend = dfs.pop()
                    visited[friend] = True
                    for nei in graph[friend]:
                        if not visited[nei]:
                            dfs.append(nei)
        
        return circles