class Solution:
    def singleNonDuplicate(self, nums):        
        
        n = len(nums)
        lo = 0
        hi = n-1
        
        while lo<hi:
            
            mid = (lo+hi)//2
            
            # check if mid is the answer
            if (mid>0 and nums[mid-1]!=nums[mid]) and (mid+1<n and nums[mid+1]!=nums[mid]):  
                return nums[mid]
            
            # mid, mid-1 are equal
            elif (mid>0 and nums[mid-1]==nums[mid]):  
                if (lo+mid+1)%2!=0: # odd elements in left half
                    hi = mid
                else:  # odd elements in right half
                    lo = mid + 1
                    
            # mid, mid+1 are equal 
            else: 
                if (hi-mid+1)%2!=0: # odd elements in right half
                    lo = mid
                else:  # odd elements in left half
                    hi = mid - 1
        
        
        return nums[lo]
            