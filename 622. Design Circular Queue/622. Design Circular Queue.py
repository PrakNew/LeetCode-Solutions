class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k
        self.queue = []
        
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.queue.append(value)
            return True
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.queue.pop(0)
            return True
        else:
            return False
        

    def Front(self):
        """
        Get the front item from the queue.
        """
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return -1
        
        
    def Rear(self):
        """
        Get the last item from the queue.
        """
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return -1
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        """
        return len(self.queue)==0
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.queue)==self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()