'''
Idea: Use sliding window of size K-1 to check if Kth current element is present in the window. Keep moving the window
      towards right. Modifying the window takes O(1) at each iteration.

Time complexity: O(n)
Space complexity: O(k)
'''

class Solution:
    def containsNearbyDuplicate(self, A, k):
        n = len(A)
        if n==0 or n==1 or k==0:
            return False
        
        start_index = min(n-1, k)
        window = set(A[:start_index])
        for i in range(start_index, n):
            if A[i] in window:
                return True
            window.remove(A[i-start_index])
            window.add(A[i])
        
        return False
