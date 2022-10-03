# My first approach was a greedy approach where I was deleting the balloons with when its next index is having similar balloon but it was giving me TLE as I was restarting from the same index after deleting
# secondly I used an approach where using 1 pointer only I was able to check which baloon needs to be removed so what I did was take the first index value in a dictionary and store its time as value now start iterating if the value you find is present already in the dictionary that means consecutive values of similar baloons are found so for that remove the minimum time to the count otherwise if no match is found in the dictionary empty the dictionary and store the new value inside it.

class Solution:
    def minCost(self, c: str, l: List[int]) -> int:
        c=list(c)
        count=0
        d = {c[0]: l[0]}
        for x in range(1,len(l)):
            if c[x] not in d:
                d = {c[x]: l[x]}
            elif l[x]>d[c[x]]:
                count+=d[c[x]]
                d[c[x]]=l[x]
            else:
                count+=l[x]
        return count
            
         