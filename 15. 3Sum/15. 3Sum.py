class Solution:
    def threeSum(self, nums):
        
        def findNSum(l, r, N, target, result, results):
            
            if N<2 or (r-l+1)<N or target < (nums[l] * N) or target > (nums[r] * N):
                return
            
            elif N==2:
                while l<r:
                    curr_sum = nums[l] + nums[r]
                    if curr_sum == target:
                        results.append(result + [nums[l]] + [nums[r]])
                        l += 1
                        while l<r and nums[l] == nums[l-1]:
                            l+=1
                        
                    elif curr_sum > target:
                        r -= 1
                    
                    else:
                        l += 1
                        
            else: # recursively call findNSum()
                for i in range(l, r+1):
                    if i==l or (i>l and nums[i]!=nums[i-1]):
                        findNSum(i+1, r, N-1, target - nums[i], result + [nums[i]], results)
        
        nums.sort()
        results = []
        findNSum(0, len(nums)-1, 3, 0, [], results)
        return results