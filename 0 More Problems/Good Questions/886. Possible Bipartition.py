from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def check(i,val):
            if i in self.group and val!=self.group[i]:
                return False
            self.group[i]=val
            if i not in self.visited:
                self.visited.add(i)
                for y in self.graph[i]:
                    if not check(y,not val):return False
            return True 
        self.graph = defaultdict(list)
        for x,y in dislikes:
            self.graph[x].append(y)
            self.graph[y].append(x)
        self.visited=set()
        self.group={}
        for i in range(1,n+1):
            if i not in self.visited:
                if not check(i,False):
                    return False
        return True
