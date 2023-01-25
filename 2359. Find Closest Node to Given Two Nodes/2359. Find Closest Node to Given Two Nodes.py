# THis is a simple DFS implementation based on the conditions provided in the question related to min and max
class Solution:
    def closestMeetingNode(self, edges: List[int], n1: int, n2: int) -> int:
        d1=defaultdict(list)
        for x in range(len(edges)):
            d1[x].append(edges[x])
        node1={}
        node2={}
        def dfs(x1,c):
            if x1 in node1:
                return 
            node1[x1]=c
            for e in d1[x1]:
                if e!=-1:
                    dfs(e,c+1)

        dfs(n1,0)
        self.final=-1
        def dfs2(x1,c):        
            if x1 in node2:
                return
            node2[x1]=c
            for e in d1[x1]:
                if e!=-1:
                    dfs2(e,c+1)

        dfs2(n2,0)
        print(node1,node2)
        reachable1=node1
        reachable2=node2
        result = float('inf')
        result_node = -1
        for node in reachable1:
            if node in reachable2:
                if result > max(reachable1[node], reachable2[node]):
                    result = max(reachable1[node], reachable2[node])
                    result_node = node
                elif result == max(reachable1[node], reachable2[node]):
                    result_node = min(node, result_node)
        return result_node