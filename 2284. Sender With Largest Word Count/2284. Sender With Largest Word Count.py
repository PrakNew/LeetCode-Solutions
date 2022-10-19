#Normal sorting based question 

from collections import defaultdict
class Solution:
    
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d=defaultdict(int)
        for ind,val in enumerate(messages):
            d[senders[ind]]+=len(val.split(' '))
        return sorted(d.items(),key = lambda x :(x[1], x[0]), reverse = True)[0][0]