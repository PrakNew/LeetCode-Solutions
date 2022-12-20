class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        s=set(rooms[0])
        visited=set()
        while s:
            for x in list(s):
                if x in visited:
                    s.remove(x)
                else:
                    visited.add(x)
                    s|=set(rooms[x])
        if 0 not in visited:visited.add(0)
        return visited==set(range(len(rooms)))
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
        