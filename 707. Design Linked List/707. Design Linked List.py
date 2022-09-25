class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(float('inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.List = []
        
    def display(self):
        for i in range(len(self.List)):
            print(self.List[i].val, end = ' ')
        print()

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index<len(self.List):
            return self.List[index].val
        return -1
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node
        self.List.insert(0, new_node)


    def addAtTail(self, val) :
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.List.append(new_node)


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < len(self.List):
            next_node = self.List[index]
            prev_node = next_node.prev
            new_node = Node(val)

            new_node.prev = prev_node
            new_node.next = next_node
            prev_node.next = new_node
            next_node.prev = new_node

            self.List.insert(index, new_node)
            
        else:
            self.addAtTail(val) 


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        if index < len(self.List):
            node = self.List[index]
            next_node = node.next
            prev_node = node.prev

            next_node.prev = prev_node
            prev_node.next = next_node
            self.List = self.List[:index] + self.List[index+1:]



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)