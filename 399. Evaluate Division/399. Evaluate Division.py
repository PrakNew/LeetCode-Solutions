import collections

class Solution:
    def calcEquation(self, equations, values, queries):
    
        graph = collections.defaultdict(list)
        ans = []
        
        for i in range(len(equations)):
            u, v = equations[i]
            val = values[i]
            graph[u] += (v, val),
            graph[v] += (u, 1/val),
        
        for start, end in queries:
            q = [(start, 1)]
            if start not in graph or end not in graph:
                ans += -1.0,
                continue
            visited = set()
            found = False
            while q:
                num, res = q.pop(0)
                visited.add(num)
                
                if num==end:
                    found = True
                    ans += res*1.0,
                    break
                
                for item in graph[num]:
                    den, frac = item[0], item[1]
                    if den not in visited:
                        q += (den, res*frac),

            if not found:
                ans += -1.0,
        
        return ans