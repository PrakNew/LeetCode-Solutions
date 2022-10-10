#simple implementation method
from collections import defaultdict
from bisect import *
class TimeMap:

    def __init__(self):
        self.d1=defaultdict(list)
        self.d2=defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        insort(self.d1[key],timestamp)
        self.d2[(key,timestamp)]=value

    def get(self, key: str, timestamp: int) -> str:
        l1=bisect(self.d1[key],timestamp)
        return "" if l1==0 else self.d2[(key,self.d1[key][l1-1])]



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