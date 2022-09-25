class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity  # capacity of cache
        self.size = 0             # current size
        self.cache = {}           # dictionary of type {int: Node}
        self.head = Node(None, None)  # pointer to head 
        self.tail = Node(None, None)  # pointer to head 

        self.head.next = self.tail  
        self.tail.prev = self.head 
    
    def addNode(self, node): 
        # Adds a node after the head 
        node.prev = self.head  
        node.next = self.head.next   

        self.head.next.prev = node 
        self.head.next = node


    def removeNode(self, node):
        # Removes the node from the list 
        prev_node = node.prev 
        next_node = node.next  

        prev_node.next = next_node
        next_node.prev = prev_node  
    
    def moveToHead(self, node):
        # Moves the given node to the head of list
        self.removeNode(node)
        self.addNode(node)
    
    def get(self, key):
        if key not in self.cache:
            return -1 
        else:
            node = self.cache[key]  
            # since node is accessed move it to the head of the list
            self.moveToHead(node)
            return node.value

    def put(self, key, value):
        if key not in self.cache:
            # create a new node and add it to the head
            node = Node(key, value)
            self.cache[key] = node  
            self.size += 1
            self.addNode(node)

            # remove the last Node if size if full
            if self.size > self.capacity: 
                last_node = self.tail.prev  
                self.removeNode(last_node) 
                del self.cache[last_node.key]   # remove node from cache
                self.size -= 1 
        
        else:
            # update the node's value
            self.cache[key].value = value
            # push it to front
            self.moveToHead(self.cache[key]) 


