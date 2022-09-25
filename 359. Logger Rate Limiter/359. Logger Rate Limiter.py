import collections

class Logger:

    def __init__(self):
        self.q = collections.defaultdict(int)
        

    def shouldPrintMessage(self, timestamp, message):
        if message in self.q and self.q[message] > timestamp:
            return False
        
        self.q[message] = timestamp + 10
        return True
        

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)