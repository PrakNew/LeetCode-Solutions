#always find the even integer index and check if its next element is same or not and make the changes accordingly
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = 2 * ((lo + hi) // 4)
            print(mid)
            if nums[mid] == nums[mid+1]:
                lo = mid+2
            else:
                hi = mid
        return nums[lo]
        return Counter(nums).most_common()[-1][0]

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
            