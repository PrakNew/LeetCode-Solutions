"""
Idea: DFS + DP

Time complexity: O(n * n * |targetPath|)
Space complexity: O(n * |targetPath|)
"""

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        
        
        def dfs(city, index):
            if dp[city][index] != -1:
                return dp[city][index]
            
            edit_dist = 0 if names[city] == targetPath[index] else 1
            
            if index == path_len - 1:
                return edit_dist
            
            # find best neighbor
            min_cost = float('inf')
            for nei in graph[city]:
                neighbor_cost = dfs(nei, index + 1)
                if neighbor_cost < min_cost:
                    min_cost = neighbor_cost
                    minCostNeighbor[city][index] = nei
            
            # update dp[][]
            edit_dist += min_cost
            dp[city][index] = edit_dist
            return edit_dist
            
        graph = collections.defaultdict(list)
        
        for a, b in roads:
            graph[a] += b,
            graph[b] += a,
        
        path_len = len(targetPath)
        dp = [[-1 for _ in range(path_len)] for _ in range(n)]
        minCostNeighbor = [[0 for _ in range(path_len)] for _ in range(n)]
        
        # DFS from every city, populate dp 
        min_cost = float('inf')
        start_city = None
        for city in range(n):
            city_res = dfs(city, 0)
            if city_res < min_cost:
                min_cost = city_res
                start_city = city
        
        res = []
        while len(res) < path_len:
            res += start_city,
            start_city = minCostNeighbor[start_city][len(res)-1]
        
        return res