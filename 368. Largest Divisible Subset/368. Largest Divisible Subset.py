class Solution:
    def largestDivisibleSubset(self, A):
        if A==[]:
            return A
        
        A.sort()
        divcount = [1] * len(A)
        max_index = 0
        prev_divisor = [-1] * len(A)
        for i in range(len(A)):
            for j in range(i):
                if A[i]%A[j]==0:
                    if divcount[i] < divcount[j]+1:
                        divcount[i] = divcount[j] + 1
                        prev_divisor[i] = j
            if divcount[max_index] < divcount[i]:
                max_index = i
                
        res = []
        k = max_index
        while k>=0:
            res += A[k],
            k = prev_divisor[k]
        
        return res
        