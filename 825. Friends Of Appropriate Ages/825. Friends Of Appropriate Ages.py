class Solution:
    def numFriendRequests(self, A):
        n = len(A)
        res = 0
        age = [0] * 121
        
        for i in A:
            age[i] += 1
            
        
        def conditions(a, b):
            return b<=(0.5*a+7) or (b>100 and a<100) or (b>a)
            
        
        for ageA, countA in enumerate(age):
            for ageB, countB in enumerate(age):
                if conditions(ageA, ageB):
                    continue
                res += countA * countB
                if ageA==ageB:
                    res -= countA
        
        return res