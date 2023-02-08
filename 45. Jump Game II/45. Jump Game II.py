# Normal greedy approach for finding the minimum count 
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:return 0
        l=[float('inf')]*n
        l[0]=0
        for x in range(len(nums)):
            if x+nums[x]>=(n-1):
                return l[x]+1
            for y in range(x+1,x+nums[x]+1):
                l[y]=min(l[y],l[x]+1)
        return l[-1] 
