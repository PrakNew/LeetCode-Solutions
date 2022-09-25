class Solution:
    def maxProduct(self, A):
        res = 0
        for i in range(len(A)):
            for j in range(len(A)):
                if i!=j and (A[i]-1)*(A[j]-1)>res:
                    res = (A[i]-1)*(A[j]-1)
        return res