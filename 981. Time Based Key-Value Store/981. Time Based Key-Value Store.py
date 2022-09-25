import collections
import bisect

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        self.dict[key].append((timestamp, value))
        

    def get(self, key, timestamp):  
        A = self.dict.get(key, None)
        if not A: 
            return ""
        
        ind = bisect.bisect(A, (timestamp, 'z'))
        return A[ind-1][1] if ind else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)