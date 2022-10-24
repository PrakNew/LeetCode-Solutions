# The main logic is to find the set intersection and check if that combination has been made or not 
# The logic is simple to iterate over the main arr list once and storing all the unions if possible in another lists



class Solution:
    def maxLength(self, arr: List[str]) -> int:
        l=[set()]
        for x in arr:
            s1=set(x)
            if len(s1)!=len(x):continue
            for y in l:
                if y&s1:continue
                l.append(s1|y)
        return max(len(x) for x in l)