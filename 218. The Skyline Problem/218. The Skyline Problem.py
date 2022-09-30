# So this is a tricky question which can be used with the logic that you have to find the contour of the diagram
# priority queue is used with the height and max heap is called 
# Certain pattern is maintained on which bases this question is solved for the reference watch this below video
# Tushar Roy video of https://www.youtube.com/watch?v=GSBLe8cKu0s

import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def check(x):
            return x[1] if x[-1] else -x[1]

        l=[]
        #0=start
        #1=end
        for x in buildings:
            l.append([x[0],x[-1],0])
            l.append([x[1],x[-1],1])
        l.sort(key=lambda x : (x[0],x[-1],check(x)))
        #print(l)
        #print()
        p=[0]
        final=[]
        for x,h,s in l:
            top=p[0]
            #print(p,[x,h,s])
            if s==0:
                heapq.heappush(p,-h)
                if p[0]!=top:
                    final.append([x,h])
            else:
                p.remove(-h)
                heapq.heapify(p)
                if p[0]!=top:
                    final.append([x,-p[0]])
            heapq.heapify(p)
        return final