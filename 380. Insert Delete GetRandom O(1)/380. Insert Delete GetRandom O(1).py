import random
#simple implementation question
class RandomizedSet:

    def __init__(self):
        self.s=set()

    def insert(self, val: int) -> bool:
        if val in self.s:return False
        self.s.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.s))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A = []
        self.pos = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos: # O(1) 
            self.A += val,      # O(1)
            self.pos[val] = len(self.A)-1
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:  # O(1)
            index, last_elem = self.pos[val], self.A[len(self.A)-1]
            self.A[index], self.pos[last_elem] = last_elem, index
            self.A.pop() # O(1)
            self.pos.pop(val)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.A[random.randint(0, len(self.A)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()