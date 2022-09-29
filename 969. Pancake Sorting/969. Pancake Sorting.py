
# there is a pattern like you have to first swap the biggest element to the first position and then swap back to the position where it actually belongs so this is how the question proceeds

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if arr==sorted(arr):
            return []
        n=len(arr)
        l=[]
        for x in range(n,0,-1):
            j=arr.index(x)
            if j==(x-1):
                continue
            if j != 0:
                l.append(j+1)
                arr=arr[:j+1][::-1]+arr[j+1:]
            l.append(x)
            arr=arr[:x][::-1]+arr[x:]
        return l


class Solution:
    def pancakeSort(self, A):
        def flip(A, k):
            i = 0
            while i < (k>>1):
                A[i], A[k-i-1] = A[k-i-1], A[i]
                i += 1
        
        element_to_sort = len(A)
        res = []
        
        while element_to_sort > 0:
            index = A.index(element_to_sort)
            
            # Make the element go to first position
            if index != element_to_sort - 1:
                if index != 0:
                    res += index + 1,
                    flip(A, index+1)

                # Make the element go to its final position
                res += element_to_sort,
                flip(A, element_to_sort)
            
            element_to_sort -= 1
        
        return res
                