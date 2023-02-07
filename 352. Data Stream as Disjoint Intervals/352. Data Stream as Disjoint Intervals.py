#direct implementation 
import bisect
class SummaryRanges:

    def __init__(self):
        self.l=[[-inf,-inf],[inf,inf]]

    def addNum(self, value: int) -> None:
        ind=bisect.bisect(self.l,[value])
        first=self.l[ind-1]
        second=self.l[ind]
        if value<=first[1] or value>=second[0]:
            pass
        elif value==first[1]+1 and value==second[0]-1:
            self.l.pop(ind)
            self.l.pop(ind-1)
            bisect.insort(self.l,[first[0],second[1]])
        elif value==first[1]+1:
            self.l.pop(ind-1)
            bisect.insort(self.l,[first[0],value])
        elif value==second[0]-1:
            self.l.pop(ind)
            bisect.insort(self.l,[value,second[1]])
        else:
            bisect.insort(self.l,[value,value])

    def getIntervals(self) -> List[List[int]]:
        return self.l[1:-1]
