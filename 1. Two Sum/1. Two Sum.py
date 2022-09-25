class Solution:
    def twoSum(self, A, target):
        
        T = {}
        
        for i in range(len(A)):
            if A[i] in T:
                return [T[A[i]], i]
            else:
                T[target-A[i]] = i
        