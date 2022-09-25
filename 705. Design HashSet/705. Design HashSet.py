class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()

    def add(self, key: int):
        if not self.contains(key):
            self.s.add(key)
        

    def remove(self, key: int):
        if self.contains(key):
            self.s.remove(key)

    def contains(self, key: int):
        """
        Returns true if this set contains the specified element
        """
        return key in self.s
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)