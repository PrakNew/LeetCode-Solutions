'''
Time complexity : O(log n)
Space complexity : O(1)
'''

def search(self, A, target):
    lo = 0
    hi = len(A)-1
    
    while lo<=hi:
        mid = (lo + hi)>>1
        
        if A[mid] == target:
            return mid
        
        # check if left half is sorted
        if A[lo]<=A[mid]:
            # check if target is in the range
            if A[lo]<=target<A[mid]:
                hi = mid
            else: # target should be in the right half
                lo = mid + 1
        
        # check if right half is sorted and target lies in righ half
        elif A[mid]<=A[hi] and A[mid]<=target<=A[hi]:
                lo = mid + 1
        
        # if both the parts seem to be unsorted, 
        # then its the middle element which is causing problem
        # remove it and recur in left half
        else:
            hi = mid-1
    
    # no element was found
    return -1
                