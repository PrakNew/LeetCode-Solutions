# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def middleNode(head):
    # Two pointers - slow and fast pointers
    slow, fast = head, head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # containts even number of elements
    return slow.next if fast.next!=None else slow
        