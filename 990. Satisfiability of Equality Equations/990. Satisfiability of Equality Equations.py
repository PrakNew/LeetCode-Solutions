'This is a graph question where I have created a graph for == and tuple for != set now simply I have applied DFS over iterating over the tuples values and checked if there is common elements between the different values of tuple'


from collections import defaultdict
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        d=defaultdict(lambda : set())
        d1=set()
        for x in equations:
            if "==" in x:
                if x[0]!=x[-1]:
                    d[x[0]].add(x[-1])
                    d[x[-1]].add(x[0])
            elif "!=" in x:
                if x[0]!=x[-1]:
                    d1.add((x[0],x[-1]))
                else:
                    return False
        def check(a,s2,d2):
            for x in d2[a]:
                if x not in s2:
                    s2.add(x)
                    check(x,s2,d2)
        #print(d,d1)   
        for x,y in d1:
            s1=set()
            check(x,s1,d)
            s=set()
            check(y,s,d)
            
            #print(x,y,s,s1)
            if s1&s!=set() :
                return False
        return True
    
            