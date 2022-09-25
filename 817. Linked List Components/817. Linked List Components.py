"""
Idea: Create a graph from the linked list. Perform DFS for every node in G

Time complexity : O(E*(V+E))
Space complexity: O(E)
"""
import collections

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head, G):
        graph = collections.defaultdict(list)
        temp = head
        while temp and temp.next:
            graph[temp.next.val] += temp.val,
            graph[temp.val] += temp.next.val,
            temp = temp.next
        
        visited = set()        
        res = 0
        
        for node in G:
            if node not in visited:
                res += 1
                q = collections.deque([node])
                visited.add(node)
                while q:
                    node = q.pop()
                    for neighbor in graph[node]:
                        if neighbor in G and neighbor not in visited:
                            q += neighbor,
                            visited.add(neighbor)
        
        return res