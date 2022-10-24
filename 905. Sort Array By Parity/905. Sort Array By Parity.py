#easy solution

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=[]
        for x in nums:
            if x%2==0:l.insert(0,x)
            else:l.append(x)
        return l


class Solution:
    def sortArrayByParity(self, A):
        i = 0
        j = 0
        n = len(A)
        
        while i < n and j < n:
            if A[j] & 1 == 0: # even
                A[i], A[j] = A[j], A[i]
                i+=1
            j+=1
        
        return A
        