# This a similar question related to resource mangement in OS where we can see the pattern
# that we have to print the longest line created joining all plantTime and growTime

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        l=list(zip(plantTime,growTime))
        l.sort(key=lambda x:-x[1])
        final=sum(l[0])
        ini=l[0][0]
        for ind in range(len(l)):
            x,y=l[ind]
            if ind==0:continue
            ini+=x
            final=max(ini+y,final)
        return final
            