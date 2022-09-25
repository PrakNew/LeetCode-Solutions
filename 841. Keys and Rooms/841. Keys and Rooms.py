import collections

class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        graph = collections.defaultdict(set)
        
        for i in range(len(rooms)):
            for key in rooms[i]:
                graph[i].add(key)
        
        visited = set()
        q = set([0])
        
        while q:
            temp = set()
            for room in q:
                visited.add(room)

                for nei in graph[room]:
                    if nei not in visited:
                        temp.add(nei)
            q = temp

        return len(visited)==n
        