class Solution:
    def findItinerary(self, tickets):
        
        graph = collections.defaultdict(list)
        
        for u, v in tickets:
            graph[u] += v,
        
        for airport in graph: # sort the destinations by lexical order
            graph[airport].sort()
        
        def dfs(airport):
            nonlocal itinerary
            while graph[airport]:
                dfs(graph[airport].pop(0))    # access the lexicographically smallest airport
            itinerary += airport,
            
        itinerary = []
        dfs('JFK')
        return itinerary[::-1]    
        