class Solution:
    def reconstructQueue(self, people):
        n = len(people)
        res = [None] * n
        
        people.sort()
        
        for h, k in people:
            i = 0
            ct = k
            while i<n and ct>0:
                if res[i]==None or res[i][0]>=h:
                    ct -= 1
                i += 1
            
            while i<n and res[i]!=None:
                i+=1

            res[i] = (h, k)
    
        return res
            