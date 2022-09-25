class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minEle = None
        

    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.minEle = x
        else:
            if x < self.minEle:
                # insert (2 * x - minEle)
                self.stack.append(2 * x - self.minEle)
                self.minEle = x
            else:
                self.stack.append(x)
        

    def pop(self):
        if self.stack:
            s = self.stack.pop()
            if s < self.minEle: # it is the minEle which is being popped
                self.minEle = 2 * self.minEle - s
                 

    def top(self):
        s = self.stack[-1]
        if s < self.minEle:
            return self.minEle 
        return s
        
        
    def getMin(self):
        return self.minEle
        
