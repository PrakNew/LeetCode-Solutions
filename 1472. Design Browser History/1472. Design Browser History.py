class BrowserHistory:

    def __init__(self, homepage: str):
        self.q = [homepage]
        self.pos = 0
        

    def visit(self, url):
        if url in self.q:
            index = self.q.index(url)
            self.q = self.q[:index+1]
            self.pos = index
        else:
            self.pos += 1
            self.q.insert(self.pos, url)
            self.q = self.q[:self.pos+1]
        

    def back(self, steps: int) -> str:
        if (self.pos - steps) < 0:
            self.pos = 0
        else:
            self.pos -= steps
    
        return self.q[self.pos]
    
        

    def forward(self, steps: int) -> str:
        if (steps + self.pos) >= len(self.q) :
            self.pos = len(self.q) - 1
        else:
            self.pos += steps
            
        return self.q[self.pos]
    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)