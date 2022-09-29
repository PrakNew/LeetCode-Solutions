# simple approach to sort zip and slicing O(nlogn)

from bisect import insort
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x1: int) -> List[int]:
        l=[0]*len(arr)
        for x in range(len(arr)):
            l[x]=arr[x]-x1
        z=list(zip(arr,l))
        z.sort(key=lambda x:(abs(x[1]),x[0]))
        l=[]
        for x in range(k):
            insort(l,z[x][0])
        return l