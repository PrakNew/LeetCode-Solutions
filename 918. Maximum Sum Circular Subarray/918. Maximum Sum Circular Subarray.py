# Kadane algorithm modification with minsum in order to work with circular condition 
class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        if max(arr)<=0:
            return max(arr)
        currmax,maxsum,currmin,minsum=[arr[0]]*4
        for x in range(1,len(arr)):
            currmax=max(currmax+arr[x],arr[x])
            maxsum=max(maxsum,currmax)
            currmin=min(currmin+arr[x],arr[x])
            minsum=min(currmin,minsum)
        return max(maxsum,sum(arr)-minsum)

class Solution:
    def maxSubarraySumCircular(self, A):
        
        all_negative = True
        
        for i in range(len(A)):
            if A[i]>=0:
                all_negative = False
                break
        
        if all_negative:
            return max(A)
        
        def kadane(A):
            max_so_far = float('-inf')
            max_here = 0
            for i in range(len(A)):
                max_here += A[i]
                if max_so_far < max_here:
                    max_so_far = max_here
                max_here = max(0, max_here)
            return max_so_far
        
        max_kadane = kadane(A)
        
        max_wrap = 0
        
        for i in range(len(A)):
            max_wrap += A[i]
            A[i] = -A[i]
        
        max_wrap = max_wrap + kadane(A)
        
        return max(max_wrap, max_kadane)
       
