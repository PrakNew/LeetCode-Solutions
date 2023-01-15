class Node:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None

class FirstUnique:

    def __init__(self, A):
        self.queue = set()
        self.cache = {} # mapping {value: Node}
        self.size = 0
        self.head = Node(float('-inf'))  # pointer to first ndoe
        self.tail = Node(float('inf'))  # pointer to last node
        
        # Connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head
        
        
        for value in A:
            
            if value not in self.queue:  # unique number
                new_node = Node(value)
                self.appendNode(new_node)
                self.cache[value] = new_node
                self.size += 1
            
            elif value in self.cache:   # not unique number
                not_unique_node = self.cache[value]
                self.removeNode(not_unique_node) # remove node from linked list
                del self.cache[value]       # remove value from cache
                self.size -= 1
            
            self.queue.add(value)
        
    def appendNode(self, node):
        
        ''' Adds node to the tail of the linked list '''
        
        node.prev = self.tail.prev
        self.tail.prev.next = node
        
        self.tail.prev = node
        node.next = self.tail
        
        
    
    def removeNode(self, node):
        
        ''' Removes node from the linked list '''
        
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
         
        

    def showFirstUnique(self):
        
        ''' Displays the node pointed by head'''
        
        if self.size==0:
            return -1
        
        first_unique_node = self.head.next
        return first_unique_node.value

        
    
    def add(self, value):
        
        ''' Check occurence of new value and add/delete'''

        if value not in self.queue:  # unique number
            new_node = Node(value)
            self.appendNode(new_node)
            self.cache[value] = new_node
            self.size += 1

        elif value in self.cache:   # not unique number
            not_unique_node = self.cache[value]
            self.removeNode(not_unique_node) # remove node from linked list
            del self.cache[value]       # remove value from cache
            self.size -= 1

        self.queue.add(value)