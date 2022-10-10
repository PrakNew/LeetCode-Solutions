#I have used used heap concept to modify the values in the list and then checking if the heap exists or not
#Python 3 solution of mine
import heapq as hq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        heap = []

        for ll in lists:
            if ll:
                hq.heappush(heap, (ll.val, id(ll), ll)) #******************id is only founded because heapq push TypeError: '<' not supported between instances was coming


        cur = head
        while heap:
            pri, idx, node = hq.heappop(heap)

            if node.next:
                hq.heappush(heap, (node.next.val, idx, node.next))

            cur.next = node
            cur = cur.next

        return head.next

#Python 2 solution
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue


        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            if node := node.next:
                q.put((node.val, node))
        return head.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        
        def merge(l1, l2):
            head = ListNode()
            temp = head

            while l1 and l2:
                if l1.val < l2.val:
                    temp.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    temp.next = ListNode(l2.val)
                    l2 = l2.next
                temp = temp.next

            while l1:
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next

            while l2:
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next

            return head.next


        while len(lists)>1:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            lists.append(merge(l1, l2))

        return lists[0] if len(lists)==1 else None