#Easy pattern solution 

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        suffix=defaultdict(lambda:set())
        for x in ideas:
            suffix[x[0]].add(x[1:])
        suffix_list=list(suffix.keys())
        sufflen=len(suffix_list)
        cnt=0
        for i in range(sufflen-1):
            for j in range(i+1,sufflen):
                set1=suffix[suffix_list[i]]
                set2=suffix[suffix_list[j]]
                cnt+=len(set1-set2)*len(set2-set1)*2
        return cnt